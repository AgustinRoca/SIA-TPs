package geneticAlgorithm.selection.roulette;

import models.player.Player;

import java.util.List;

public class Boltzmann extends Roulette {
    private static final double TC = 500;
    private static final double T0 = 20;
    private static final double K = 10;

    @Override
    double aptitude(int i, List<Player> players, int generation) {
        double accum = 0;
        for (Player player : players){
            accum += Math.exp(player.fitness()/getTemperature(generation));
        }
        double avg = accum / players.size();
        return Math.exp(players.get(i).fitness()/getTemperature(generation))/avg;
    }

    private double getTemperature(int generation){
        return TC +  (T0 - TC) * Math.exp(-K*generation);
    }
}
