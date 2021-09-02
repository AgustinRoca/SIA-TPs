package geneticAlgorithm.selection.roulette;

import models.player.Player;
import geneticAlgorithm.selection.SelectionMethod;

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.Collectors;

public class Roulette implements SelectionMethod {

    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        // TODO: Fix initial capacity
        List<Player> playerList = new ArrayList<>(players);
        Map<Double, Player> slices = slices(playerList, generation);

        List<Player> selectedPlayers = new LinkedList<>();
        for (int selectionNumber = 0; selectionNumber < k; selectionNumber++) {
            double sliceSelected = 0;
            double randomSelector = randomGenerator(selectionNumber, k);
            for(Double slice : slices.keySet().stream().sorted().collect(Collectors.toList())){
                if(randomSelector <= slice){
                    sliceSelected = slice;
                    break;
                }
            }
            selectedPlayers.add(slices.get(sliceSelected));
        }
        return selectedPlayers;
    }

    private Map<Double, Player> slices(List<Player> players, int generation){
        players.sort(Comparator.reverseOrder());
        double fitnessSum = 0;
        for (int i = 0; i < players.size(); i++) {
            fitnessSum += aptitude(i, players, generation);
        }

        Map<Double, Player> sliceProportions = new HashMap<>();
        double sliceAccum = 0;
        for (int i = 0; i < players.size(); i++) {
            double aptitude = aptitude(i, players, generation) / fitnessSum;
            sliceAccum += aptitude;
            if (aptitude > 0) {
                sliceProportions.put(sliceAccum, players.get(i));
            }
        }
        return sliceProportions;
    }

    double randomGenerator(int i, int k){
        return ThreadLocalRandom.current().nextDouble();
    }

    double aptitude(int i, List<Player> players, int generation){
        return players.get(i).fitness();
    }
}
