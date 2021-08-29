package selection.roulette;

import models.player.Player;

import java.util.ArrayList;
import java.util.List;

public class Boltzmann extends Roulette {
    private static final double TC = 500;
    private static final double T0 = 20;
    private static final double K = 10;

    @Override
    List<Double> slices(List<Player> players, int generation){
        List<Double> aptitudes = aptitudes(players, generation);
        double aptitudesSum = aptitudes(players, generation).stream().reduce(0.0, Double::sum);

        List<Double> sliceProportions = new ArrayList<>();
        double sliceAccum = 0;
        for (int i = 0; i<players.size(); i++){
            sliceAccum += aptitudes.get(i) / aptitudesSum;
            sliceProportions.add(sliceAccum);
        }
        return sliceProportions;
    }

    private List<Double> aptitudes(List<Player> players, int generation){
        List<Double> aptitudes = new ArrayList<>();
        double temperature = getTemperature(generation);
        double accum = 0;
        for (Player player : players) {
            accum += Math.exp(player.fitness() / temperature);
        }
        double avg = accum / players.size();
        for (Player player : players) {
            aptitudes.add(Math.exp(player.fitness() / temperature) / avg);
        }
        return aptitudes;
    }

    private double getTemperature(int generation){
        return TC +  (T0 - TC) * Math.exp(-K*generation);
    }
}
