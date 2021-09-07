package geneticAlgorithm.selection.roulette;

import models.player.Player;

import java.util.ArrayList;
import java.util.List;

public class Boltzmann extends Roulette {
    private final double tc;
    private final double t0;
    private final double k;

    public Boltzmann(double k, double t0, double tc) {
        this.k = k;
        this.t0 = t0;
        this.tc = tc;
    }

    @Override
    double aptitude(int i, ArrayList<Player> players, int generation) {
        double accum = 0;
        for (Player player : players){
            accum += Math.exp(player.fitness() / getTemperature(generation));
        }

        double avg = accum / players.size();
        return Math.exp(players.get(i).fitness() / getTemperature(generation)) / avg;
    }

    private double getTemperature(int generation){
        return tc + (t0 - tc) * Math.exp(-k * generation);
    }
}
