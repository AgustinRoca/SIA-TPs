package engine;

import criteria.*;
import fill.FillAll;
import fill.FillMethod;
import fill.FillParent;
import geneticOperators.mutation.*;
import models.config.*;
import models.player.Player;
import selection.*;
import selection.roulette.Boltzmann;
import selection.roulette.Ranking;
import selection.roulette.Roulette;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;

public class Engine {
    public static Player start(List<Player> population, Config config) {
        Selector selectionSelector = getSelector(config.getSelectionConfig(), config, config.getPlayerConfig().getSelection());
        FillMethod filler = getFiller(config);

        StopCriteria criteria = getStopCriteria(config.getStopCriteriaConfig());
        StopCriteriaData data = new StopCriteriaData(config.getStopCriteriaConfig().getPercentage(), config.getPlayerConfig().getCount());
        data.addGeneration(population);
        while (!criteria.shouldStop(data)){
            Collection<Player> parents = selectionSelector.select(data.getLastGeneration(), data.getGenerations().size());
            List<Player> children = new ArrayList<>();

            if(config.getOperationConfig().getType() == OperationConfig.OperationType.MUTATION){
                Mutation mutation = getMutation(config.getMutationConfig());
                for(Player parent : parents){
                    children.add(mutation.mutate(parent));
                }
            } else {
                // TODO: Juntar parents de dos en dos y cruzar
            }
            Collection<Player> newGeneration = filler.getGeneration(data.getLastGeneration(),
                    children, data.getGenerationsQuantity() + 1);
            data.addGeneration(newGeneration);
            // TODO: graphs
            System.out.println("Best of generation " + data.getGenerations().size() + ": " + data.getLastGeneration().get(0));
        }
        return data.getLastGeneration().get(0);
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
        models.config.FillMethod fillMethod = config.getFillMethod();
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
