package geneticAlgorithm.selection.tournament;

import models.player.Player;
import geneticAlgorithm.selection.SelectionMethod;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public abstract class Tournament implements SelectionMethod {
    private final int playersInMatch;

    protected Tournament(int playersInMatch) {
        this.playersInMatch = playersInMatch;
    }

    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        List<Player> playerList = new ArrayList<>(players);
        List<Player> selected = new ArrayList<>(k);
        for (int i = 0; i < k; i++) {
            selected.add(getWinner(getRandomPlayers(playerList, playersInMatch)));
        }
        return selected;
    }

    abstract Player getWinner(Collection<Player> players);

    private Collection<Player> getRandomPlayers(List<Player> players, int quantity){
        List<Player> randomPlayers = new ArrayList<>(quantity);
        for (int i = 0; i < quantity; i++) {
            randomPlayers.add(players.get(ThreadLocalRandom.current().nextInt(players.size())));
        }
        return randomPlayers;
    }
}
