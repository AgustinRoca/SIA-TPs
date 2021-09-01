package selection.roulette;

import models.player.Player;
import selection.SelectionMethod;

import java.util.*;
import java.util.concurrent.Callable;
import java.util.function.Function;

public class Roulette implements SelectionMethod {

    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        List<Player> playerList = new ArrayList<>(players);
        Map<Double, Player> slices = slices(playerList, generation);

        List<Player> selectedPlayers = new LinkedList<>();
        double sliceSelected = 0;
        for (int selectionNumber = 0; selectionNumber < k; selectionNumber++) {
            double randomSelector = randomGenerator(selectionNumber, k);
            for(Double slice : slices.keySet()){
                if(randomSelector > slice && slice > sliceSelected){
                    sliceSelected = slice;
                }
            }
            selectedPlayers.add(slices.get(sliceSelected));
        }
        return selectedPlayers;
    }

    Map<Double, Player> slices(List<Player> players, int generation){
        players.sort(Comparator.reverseOrder());
        double fitnessSum = 0;
        for (int i = 0; i < players.size(); i++) {
            fitnessSum += aptitude(i, players, generation);
        }

        Map<Double, Player> sliceProportions = new HashMap<>();
        List<Player> playerList = new ArrayList<>(players);
        double sliceAccum = 0;
        for (Player player : playerList){
            sliceAccum += player.fitness() / fitnessSum;
            sliceProportions.put(sliceAccum, player);
        }
        return sliceProportions;
    }

    double randomGenerator(int i, int k){
        return Math.random();
    }

    double aptitude(int i, List<Player> players, int generation){
        return players.get(i).fitness();
    }
}
