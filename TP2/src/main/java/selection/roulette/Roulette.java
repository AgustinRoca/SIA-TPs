package selection.roulette;

import models.player.Player;
import selection.SelectionMethod;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

public class Roulette implements SelectionMethod {
    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        List<Player> playerList = new ArrayList<>(players);
        List<Double> slices = slices(playerList, generation);

        List<Player> selectedPlayers = new LinkedList<>();
        for (int selectionNumber = 0; selectionNumber < k; selectionNumber++) {
            double randomSelection = Math.random();
            Player selectedPlayer = playerList.get(0);
            for (int sliceNumber = 1; sliceNumber < slices.size() && randomSelection < slices.get(sliceNumber); sliceNumber++) {
                selectedPlayer = playerList.get(sliceNumber);
            }
            selectedPlayers.add(selectedPlayer);
        }
        return selectedPlayers;
    }

    List<Double> slices(List<Player> players, int generation){
        double fitnessSum = players.stream().map(Player::fitness).reduce(0.0, Double::sum);

        List<Double> sliceProportions = new ArrayList<>();
        List<Player> playerList = new ArrayList<>(players);
        double sliceAccum = 0;
        for (Player player : playerList){
            sliceAccum += player.fitness() / fitnessSum;
            sliceProportions.add(sliceAccum);
        }
        return sliceProportions;
    }
}
