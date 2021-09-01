package engine;

import criteria.*;
import fill.FillAll;
import fill.FillMethod;
import fill.FillParent;
import models.config.Config;
import models.config.SelectionReplacementConfig;
import models.config.StopCriteriaConfig;
import models.player.Player;
import selection.*;
import selection.roulette.Boltzmann;
import selection.roulette.Ranking;
import selection.roulette.Roulette;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Engine {
    public static Player start(List<Player> population, Config config) {
        List<Player> children, parents;
        Selector selectionSelector = getSelector(config.getSelectionConfig(), config, config.getPlayerConfig().getSelection());
        FillMethod filler = getFiller(config);

        StopCriteria criteria = getStopCriteria(config.getStopCriteriaConfig());
        StopCriteriaData data = new StopCriteriaData(config.getStopCriteriaConfig().getPercentage(), config.getPlayerConfig().getCount());
        while (!criteria.shouldStop(data)){
            // TODO: select parents
            // TODO: cross or mutate last generation
            // TODO: fill new generation
            // TODO: update StopCriteriaData
            // TODO: graphs
        }
        return data.getGenerations().get(0).get(0);
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
