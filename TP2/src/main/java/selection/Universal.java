package selection;

import models.player.Player;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

public class Universal implements SelectionMethod {
    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        double fitnessSum = players.stream().map(Player::fitness).reduce(0.0, Double::sum);

        List<Double> sliceProportions = new ArrayList<>();
        List<Player> playerList = new ArrayList<>(players);
        double sliceAccum = 0;
        for (Player player : playerList){
            sliceAccum += player.fitness() / fitnessSum;
            sliceProportions.add(sliceAccum);
        }
        List<Player> selectedPlayers = new LinkedList<>();
        double randomNumber = Math.random();
        for (int selectionNumber = 0; selectionNumber < k; selectionNumber++) {
            double randomSelection = (randomNumber + selectionNumber)/k;
            Player selectedPlayer = playerList.get(0);
            for (int sliceNumber = 1; sliceNumber < sliceProportions.size() && randomSelection < sliceProportions.get(sliceNumber); sliceNumber++) {
                selectedPlayer = playerList.get(sliceNumber);
            }
            selectedPlayers.add(selectedPlayer);
        }
        return selectedPlayers;
    }
}
