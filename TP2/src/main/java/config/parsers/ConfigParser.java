package config.parsers;

import config.containers.*;
import config.containers.CrossoverConfig.CrossoverType;
import config.containers.MutationConfig.MutationType;
import config.containers.SelectionReplacementConfig.SelectionReplacementMethod;
import config.containers.StopCriteriaConfig.StopCriteriaType;
import models.equipment.*;
import models.player.*;
import org.json.JSONObject;
import org.json.JSONTokener;

import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

public abstract class ConfigParser {
    public static void parse(InputStream stream) throws IllegalArgumentException {
        JSONObject json = new JSONObject(new JSONTokener(stream));

        Config config = Config.getInstance();

        try {
            config.setOutputPath(json.getString("outputPath"));
            config.setFillMethod(json.getEnum(FillMethod.class, "fillMethod"));

            config.setPlayerConfig(ConfigParser.getPlayerConfig(json.getJSONObject("player")));
            config.setEquipmentConfig(ConfigParser.getEquipmentConfig(json.getJSONObject("equipment")));

            JSONObject mutation = json.getJSONObject("mutation");
            config.setMutationConfig(ConfigParser.getMutationConfig(mutation));

            JSONObject crossover = json.getJSONObject("crossover");
            config.setCrossoverConfig(ConfigParser.getCrossoverConfig(crossover));

            config.setStopCriteriaConfig(ConfigParser.getStopCriteriaConfig(json.getJSONObject("stopCriteria")));
            config.setSelectionConfig(ConfigParser.getSelectionReplacementConfig(json.getJSONObject("selection")));
            config.setReplacementConfig(ConfigParser.getSelectionReplacementConfig(json.getJSONObject("replacement")));

            if (ConfigParser.hasToParseTournamentProbabilisticConfig()) {
                config.setProbabilisticTournamentConfig(ConfigParser.getTournamentProbabilisticConfig(json.getJSONObject("tournamentProbabilistic")));
            }
            if (ConfigParser.hasToParseTournamentDeterministicConfig()) {
                config.setDeterministicTournamentConfig(ConfigParser.getTournamentDeterministicConfig(json.getJSONObject("tournamentDeterministic")));
            }
            if (ConfigParser.hasToParseBoltzmannConfig()) {
                config.setBoltzmannConfig(ConfigParser.getBoltzmannConfig(json.getJSONObject("boltzmann")));
            }
        } catch (Exception e) {
            throw new IllegalArgumentException(e);
        }
    }

    private static PlayerConfig getPlayerConfig(JSONObject json) {
        return new PlayerConfig(
                ConfigParser.getPlayerClass(json.getString("type")),
                json.getInt("count"),
                json.getInt("selection"),
                ConfigParser.getHeightConfig(json.getJSONObject("height"))
        );
    }

    private static Class<? extends Player> getPlayerClass(String player) {
        switch (player.toUpperCase()) {
            case "WARRIOR": return Warrior.class;
            case "ARCHER": return Archer.class;
            case "UNDERCOVER": return Undercover.class;
            case "DEFENDER": return Defender.class;
            default: throw new IllegalArgumentException();
        }
    }

    private static HeightConfig getHeightConfig(JSONObject json) {
        if (json.has("random")) {
            return HeightConfig.random();
        } else if (json.has("increment")) {
            return HeightConfig.increment(json.getDouble("increment"));
        } else if (json.has("precalculated")) {
            return HeightConfig.precalculated();
        } else {
            throw new IllegalArgumentException();
        }
    }

    private static EquipmentConfig getEquipmentConfig(JSONObject json) {
        JSONObject filesJson = json.getJSONObject("files");
        Map<Class<? extends Equipment>, String> files = new HashMap<>();

        String prefix;
        if (filesJson.has("prefix")) {
            prefix = filesJson.getString("prefix");
            if (!prefix.endsWith("/"))
                prefix += "/";
        } else {
            prefix = "";
        }

        files.put(Boots.class, prefix + filesJson.getString("boots"));
        files.put(Gloves.class, prefix + filesJson.getString("gloves"));
        files.put(Helmet.class, prefix + filesJson.getString("helmet"));
        files.put(Vest.class, prefix + filesJson.getString("vest"));
        files.put(Weapon.class, prefix + filesJson.getString("weapon"));

        Map<Class<? extends Equipment>, Integer> equipments = new HashMap<>();
        if (json.has("items")) {
            JSONObject items = json.getJSONObject("items");

            if (items.has("boots")) equipments.put(Boots.class, items.getInt("boots"));
            if (items.has("gloves")) equipments.put(Gloves.class, items.getInt("gloves"));
            if (items.has("helmet")) equipments.put(Helmet.class, items.getInt("helmet"));
            if (items.has("vest")) equipments.put(Vest.class, items.getInt("vest"));
            if (items.has("weapon")) equipments.put(Weapon.class, items.getInt("weapon"));
        }

        return new EquipmentConfig(
                json.getBoolean("inMemory"),
                files,
                equipments
        );
    }

    private static MutationConfig getMutationConfig(JSONObject json) {
        double probability = json.getDouble("probability");
        MutationType type = MutationType.valueOf(json.getString("type"));

        if (type == MutationType.MULTIGEN_LIMITED || type == MutationType.MULTIGEN_UNIFORM) {
            return new MultigenMutationConfig(
                    type,
                    probability,
                    json.getInt("multigenLimitedM")
            );
        } else {
            return new MutationConfig(
                    type,
                    probability
            );
        }
    }

    private static CrossoverConfig getCrossoverConfig(JSONObject json) {
        CrossoverType type = CrossoverType.valueOf(json.getString("type"));

        if (type == CrossoverType.UNIFORM) {
            return new UniformCrossoverConfig(
                    json.getDouble("probability")
            );
        } else {
            return new CrossoverConfig(
                    type
            );
        }
    }

    private static StopCriteriaConfig getStopCriteriaConfig(JSONObject json) {
        StopCriteriaType type = StopCriteriaType.valueOf(json.getString("criteria"));
        String stopCriteriaParameterName = "parameter";
        if (type == StopCriteriaType.STRUCTURE) {
            return new StopCriteriaConfig(type,
                    json.getInt(stopCriteriaParameterName),
                    json.getDouble("percentage")
            );
        } else if (type == StopCriteriaType.TIMEOUT) {
            return new StopCriteriaConfig(
                    type,
                    json.getLong(stopCriteriaParameterName),
                    0
            );
        } else if (type == StopCriteriaType.ACCEPTABLE_SOLUTION) {
            return new StopCriteriaConfig(
                    type,
                    json.getDouble(stopCriteriaParameterName),
                    0
            );
        } else {
            return new StopCriteriaConfig(
                    type,
                    json.getInt(stopCriteriaParameterName),
                    0
            );
        }
    }

    private static SelectionReplacementConfig getSelectionReplacementConfig(JSONObject json) {
        return new SelectionReplacementConfig(
                SelectionReplacementMethod.valueOf(json.getString("methodA")),
                SelectionReplacementMethod.valueOf(json.getString("methodB")),
                json.getDouble("factor")
        );
    }

    private static ProbabilisticTournamentConfig getTournamentProbabilisticConfig(JSONObject json) {
        return new ProbabilisticTournamentConfig(json.getDouble("probability"));
    }

    private static DeterministicTournamentConfig getTournamentDeterministicConfig(JSONObject json) {
        return new DeterministicTournamentConfig(json.getInt("window"));
    }

    private static BoltzmannConfig getBoltzmannConfig(JSONObject json) {
        return new BoltzmannConfig(
                json.getDouble("k"),
                json.getDouble("t0"),
                json.getDouble("tc")
        );
    }

    private static boolean hasToParseTournamentProbabilisticConfig() {
        Config config = Config.getInstance();

        return  config.getSelectionConfig().getMethodA() == SelectionReplacementMethod.TOURNAMENT_PROBABILISTIC
                || config.getSelectionConfig().getMethodB() == SelectionReplacementMethod.TOURNAMENT_PROBABILISTIC
                || config.getReplacementConfig().getMethodA() == SelectionReplacementMethod.TOURNAMENT_PROBABILISTIC
                || config.getReplacementConfig().getMethodB() == SelectionReplacementMethod.TOURNAMENT_PROBABILISTIC;
    }

    private static boolean hasToParseTournamentDeterministicConfig() {
        Config config = Config.getInstance();

        return  config.getSelectionConfig().getMethodA() == SelectionReplacementMethod.TOURNAMENT_DETERMINISTIC
                || config.getSelectionConfig().getMethodB() == SelectionReplacementMethod.TOURNAMENT_DETERMINISTIC
                || config.getReplacementConfig().getMethodA() == SelectionReplacementMethod.TOURNAMENT_DETERMINISTIC
                || config.getReplacementConfig().getMethodB() == SelectionReplacementMethod.TOURNAMENT_DETERMINISTIC;
    }

    private static boolean hasToParseBoltzmannConfig() {
        Config config = Config.getInstance();

        return  config.getSelectionConfig().getMethodA() == SelectionReplacementMethod.BOLTZMANN
                || config.getSelectionConfig().getMethodB() == SelectionReplacementMethod.BOLTZMANN
                || config.getReplacementConfig().getMethodA() == SelectionReplacementMethod.BOLTZMANN
                || config.getReplacementConfig().getMethodB() == SelectionReplacementMethod.BOLTZMANN;
    }
}
