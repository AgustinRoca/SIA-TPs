package engine;

import config.containers.OperationConfig.OperationType;
import geneticAlgorithm.stopCriteria.*;
import geneticAlgorithm.fill.*;
import geneticAlgorithm.fill.FillMethod;
import geneticAlgorithm.geneticOperators.crossover.*;
import geneticAlgorithm.geneticOperators.mutation.*;
import config.containers.*;
import models.player.Player;
import geneticAlgorithm.selection.*;
import geneticAlgorithm.selection.roulette.*;
import geneticAlgorithm.selection.tournament.*;
import serializer.GenerationSerializer;

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class Engine {
    private final GenerationSerializer generationSerializer;

    public Engine(GenerationSerializer generationSerializer) {
        this.generationSerializer = generationSerializer;
    }

    public Player run(List<Player> population) {
        Config config = Config.getInstance();

        int k = config.getPlayerConfig().getSelection();
        int n = config.getPlayerConfig().getCount();
        Selector selectionSelector = getSelector(config.getSelectionConfig(), config, k);
        FillMethod filler = getFiller(config);

        StopCriteria criteria = getStopCriteria(config.getStopCriteriaConfig());
        StopCriteriaData data = new StopCriteriaData(config.getStopCriteriaConfig().getPercentage(), n);
        data.addGeneration(population);

        Mutation mutation;
        Crossover crossover;
        if (config.getOperationConfig().getType() == OperationType.MUTATION) {
            mutation = getMutation(config.getMutationConfig());
            crossover = null;
        } else {
            crossover = getCrossover(config.getCrossoverConfig());
            mutation = null;
        }

        while (!criteria.shouldStop(data)){
            this.generationSerializer.serialize(data.getGenerationsQuantity(), data.getLastGeneration());

            Collection<Player> parents = selectionSelector.select(data.getLastGeneration(), data.getGenerationsQuantity());
            List<Player> children = new ArrayList<>(data.getLastGeneration().size());

            if (mutation != null) {
                for (Player parent : parents) {
                    children.add(mutation.mutate(parent));
                }
            } else {
                Random random = ThreadLocalRandom.current();

                List<Player> auxParents = new LinkedList<>(parents);
                Collections.shuffle(auxParents, random);
                List<List<Player>> pairParents = new ArrayList<>(parents.size() / 2);

                for (int i = 0; i < parents.size() / 2; i++) {
                    ArrayList<Player> aux = new ArrayList<>();
                    pairParents.add(aux);
                    aux.add(auxParents.remove(0));
                    aux.add(auxParents.remove(0));
                }

                for (List<Player> pairParent : pairParents){
                    children.addAll(Arrays.asList(crossover.cross(pairParent.get(0), pairParent.get(1))));
                }
            }

            Collection<Player> newGeneration = filler.getGeneration(data.getLastGeneration(),
                    children, data.getGenerationsQuantity() + 1);

            data.addGeneration(newGeneration);
        }

        this.generationSerializer.serialize(data.getGenerationsQuantity(), data.getLastGeneration());

        return data.getLastGeneration().get(0);
    }

    private static Crossover getCrossover(CrossoverConfig config) {
        switch (config.getType()){
            case SINGLE_POINT:
                return new OnePointCrossover();
            case TWO_POINTS:
                return new TwoPointCrossover();
            case UNIFORM:
                UniformCrossoverConfig uniformCrossoverConfig = (UniformCrossoverConfig) config;
                return new UniformCrossover(uniformCrossoverConfig.getProbability());
            case ANNULAR:
                return new AnnularCrossover();
        }
        throw new RuntimeException(config.getType() + " is not a valid crossover type");
    }

    private static Mutation getMutation(MutationConfig config) {
        switch (config.getType()){
            case GEN:
                return new GeneMutation(config.getProbability(), true, 0);
            case COMPLETE:
                return new CompleteMutation(config.getProbability(), true, 0);
            case MULTIGEN_LIMITED:
                return new LimitedMutation(config.getProbability(), true, 0);
            case MULTIGEN_UNIFORM:
                return new UniformMutation(config.getProbability(), true, 0);
        }
        throw new RuntimeException(config.getType() + " is not a valid mutation type");
    }

    private static StopCriteria getStopCriteria(StopCriteriaConfig config) {
        switch (config.getType()){
            case GENERATIONS:
                return new GenerationStopCriteria(config.getParameter().intValue());
            case TIMEOUT:
                return new TimeStopCriteria(config.getParameter().longValue());
            case ACCEPTABLE_SOLUTION:
                return new FitnessStopCriteria(config.getParameter().doubleValue());
            case CONTENT:
                return new StableStopCriteria(config.getParameter().intValue());
            case STRUCTURE:
                return new PercentageStableStopCriteria(config.getParameter().intValue());
        }
        throw new IllegalArgumentException(config.getType() + " is not a valid Stop criteria");
    }

    private static FillMethod getFiller(Config config) {
        config.containers.FillMethod fillMethod = config.getFillMethod();
        switch (fillMethod){
            case ALL:
                return new FillAll(getSelector(config.getReplacementConfig(), config, config.getPlayerConfig().getCount()));
            case PARENTS:
                SelectionMethod selectionMethod1 = getSelectionMethod(config.getReplacementConfig().getMethodA(), config);
                SelectionMethod selectionMethod2 = getSelectionMethod(config.getReplacementConfig().getMethodA(), config);
                double a = config.getSelectionConfig().getFactor();
                int n = config.getPlayerConfig().getCount();
                int k = config.getPlayerConfig().getSelection();
                return new FillParent(selectionMethod1, selectionMethod2, a, k, n);
        }
        throw new IllegalArgumentException(fillMethod + " is not a valid Fill method");
    }

    private static Selector getSelector(SelectionReplacementConfig selectionConfig, Config config, int k) {
        SelectionMethod selectionMethodA = getSelectionMethod(selectionConfig.getMethodA(), config);
        SelectionMethod selectionMethodB = getSelectionMethod(selectionConfig.getMethodB(), config);
        double selectionProb = selectionConfig.getFactor();
        return new Selector(selectionMethodA, selectionMethodB, selectionProb, k);
    }

    private static SelectionMethod getSelectionMethod(SelectionReplacementConfig.SelectionReplacementMethod selectionMethod, Config config) {
        switch (selectionMethod){
            case ELITE:
                return new Elite();
            case ROULETTE:
                return new Roulette();
            case UNIVERSAL:
                return new Universal();
            case BOLTZMANN:
                return new Boltzmann();
            case TOURNAMENT_DETERMINISTIC:
                return new DeterministicTournament(config.getDeterministicTournamentConfig().getPlayersInMatch());
            case TOURNAMENT_PROBABILISTIC:
                return new ProbabilisticTournament(config.getProbabilisticTournamentConfig().getProbability());
            case RANKING:
                return new Ranking();
        }
        throw new RuntimeException(selectionMethod + " is not a valid selection method");
    }


}
