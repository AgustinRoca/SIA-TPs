package parsers;

import models.config.*;
import models.config.CrossoverConfig.CrossoverType;
import models.config.MutationConfig.MutationType;
import models.config.SelectionReplacementConfig.SelectionReplacementMethod;
import models.config.StopCriteriaConfig.StopCriteriaType;
import models.player.*;
import org.json.JSONObject;
import org.json.JSONTokener;

import java.io.InputStream;

public abstract class ConfigParser {
    private static final String STOP_CRITERIA_PARAMETER_NAME = "parameter";

    public static void parse(InputStream stream) throws IllegalArgumentException {
        JSONObject json = new JSONObject(new JSONTokener(stream));

        Config config = Config.getInstance();

        try {
            config.setOutputPath(json.getString("outputPath"));
            config.setFillMethod(json.getEnum(FillMethod.class, "fillMethod"));

            config.setPlayerConfig(ConfigParser.getPlayerConfig(json.getJSONObject("player")));
            config.setEquipmentConfig(ConfigParser.getEquipmentConfig(json.getJSONObject("equipment")));
            config.setMutationConfig(ConfigParser.getMutationConfig(json.getJSONObject("mutation")));
            config.setCrossoverConfig(ConfigParser.getCrossoverConfig(json.getJSONObject("crossover")));
            config.setStopCriteriaConfig(ConfigParser.getStopCriteriaConfig(json.getJSONObject("stopCriteria")));
            config.setSelectionConfig(ConfigParser.getSelectionReplacementConfig(json.getJSONObject("selection")));
            config.setReplacementConfig(ConfigParser.getSelectionReplacementConfig(json.getJSONObject("replacement")));

            if (ConfigParser.hasToParseTournamentProbabilisticConfig()) {
                config.setTournamentConfig(ConfigParser.getTournamentProbabilisticConfig(json.getJSONObject("tournamentProbabilistic")));
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
        switch (player) {
            case "WARRIOR": return Warrior.class;
            case "ARCHER": return Archer.class;
            case "UNDERCOVER": return Undercover.class;
            case "DEFENDER": return Defender.class;
            default: throw new IllegalArgumentException();
        }
    }

    private static HeightConfig getHeightConfig(JSONObject json) {
        if (json.getBoolean("random")) {
            return new HeightConfig();
        } else {
            JSONObject interval = json.getJSONObject("interval");

            return new HeightConfig(
                    interval.getDouble("min"),
                    interval.getDouble("max"),
                    json.getDouble("direction")
            );
        }
    }

    private static EquipmentConfig getEquipmentConfig(JSONObject json) {
        return new EquipmentConfig(
                json.getBoolean("inMemory"),
                json.getString("boots"),
                json.getString("gloves"),
                json.getString("helmet"),
                json.getString("vest"),
                json.getString("weapon")
        );
    }

    private static MutationConfig getMutationConfig(JSONObject json) {
        double probability = json.getDouble("probability");
        MutationType type = json.getEnum(MutationType.class, json.getString("type"));

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
        CrossoverType type = json.getEnum(CrossoverType.class, json.getString("type"));

        if (type == CrossoverType.UNIFORM) {
            return new UniformCrossoverConfig(
                    json.getDouble("probability"),
                    json.getDouble("threshold")
            );
        } else {
            return new CrossoverConfig(
                    type
            );
        }
    }

    private static StopCriteriaConfig getStopCriteriaConfig(JSONObject json) {
        StopCriteriaType type = json.getEnum(StopCriteriaType.class, json.getString("type"));

        if (type == StopCriteriaType.STRUCTURE) {
            return new StructureStopCriteriaConfig(
                    json.getInt(STOP_CRITERIA_PARAMETER_NAME),
                    json.getDouble("percentage")
            );
        } else if (type == StopCriteriaType.TIMEOUT) {
            return new StopCriteriaConfig(
                    type,
                    json.getLong(STOP_CRITERIA_PARAMETER_NAME)
            );
        } else if (type == StopCriteriaType.ACCEPTABLE_SOLUTION) {
            return new StopCriteriaConfig(
                    type,
                    json.getDouble(STOP_CRITERIA_PARAMETER_NAME)
            );
        } else {
            return new StopCriteriaConfig(
                    type,
                    json.getInt(STOP_CRITERIA_PARAMETER_NAME)
            );
        }
    }

    private static SelectionReplacementConfig getSelectionReplacementConfig(JSONObject json) {
        return new SelectionReplacementConfig(
                json.getEnum(SelectionReplacementMethod.class, "methodA"),
                json.getEnum(SelectionReplacementMethod.class, "methodB"),
                json.getDouble("factor")
        );
    }

    private static ProbabilisticTournamentConfig getTournamentProbabilisticConfig(JSONObject json) {
        return new ProbabilisticTournamentConfig(
                json.getDouble("probability"),
                json.getInt("window")
        );
    }

    private static BoltzmannConfig getBoltzmannConfig(JSONObject json) {
        return new BoltzmannConfig(
                json.getDouble("t0"),
                json.getDouble("tk")
        );
    }

    private static boolean hasToParseTournamentProbabilisticConfig() {
        Config config = Config.getInstance();

        return  config.getSelectionConfig().getMethodA() == SelectionReplacementMethod.TOURNAMENT_PROBABILISTIC
                || config.getSelectionConfig().getMethodB() == SelectionReplacementMethod.TOURNAMENT_PROBABILISTIC
                || config.getReplacementConfig().getMethodA() == SelectionReplacementMethod.TOURNAMENT_PROBABILISTIC
                || config.getReplacementConfig().getMethodB() == SelectionReplacementMethod.TOURNAMENT_PROBABILISTIC;
    }

    private static boolean hasToParseBoltzmannConfig() {
        Config config = Config.getInstance();

        return  config.getSelectionConfig().getMethodA() == SelectionReplacementMethod.BOLTZMANN
                || config.getSelectionConfig().getMethodB() == SelectionReplacementMethod.BOLTZMANN
                || config.getReplacementConfig().getMethodA() == SelectionReplacementMethod.BOLTZMANN
                || config.getReplacementConfig().getMethodB() == SelectionReplacementMethod.BOLTZMANN;
    }
}
