package selection.roulette;

import models.player.Player;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Ranking extends Roulette{
    @Override
    List<Double> slices(List<Player> players, int generation){
        List<Double> aptitudes = aptitudes(players);
        double aptitudesSum = aptitudes(players).stream().reduce(0.0, Double::sum);

        List<Double> sliceProportions = new ArrayList<>();
        double sliceAccum = 0;
        for (int i = 0; i<players.size(); i++){
            sliceAccum += aptitudes.get(i) / aptitudesSum;
            sliceProportions.add(sliceAccum);
        }
        return sliceProportions;
    }

    private List<Double> aptitudes(List<Player> players){
        players.sort(Comparator.reverseOrder());
        List<Double> aptitudes = new ArrayList<>();
        for (int i = 0; i<players.size(); i++){
            aptitudes.add(1 - (double) i/players.size());
        }
        return aptitudes;
    }
}
