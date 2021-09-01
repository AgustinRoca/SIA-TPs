package selection.tournament;

import models.player.Player;
import selection.SelectionMethod;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public abstract class Tournament implements SelectionMethod {
    private final int playersInMatch;

    protected Tournament(int playersInMatch) {
        this.playersInMatch = playersInMatch;
    }

    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        List<Player> playerList = new ArrayList<>(players);
        List<Player> selected = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            selected.add(getWinner(getRandomPlayers(playerList, playersInMatch)));
        }
        return selected;
    }

    abstract Player getWinner(Collection<Player> players);

    private Collection<Player> getRandomPlayers(List<Player> players, int quantity){
        List<Player> randomPlayers = new ArrayList<>();
        for (int i = 0; i < quantity; i++) {
            randomPlayers.add(players.get((int) Math.floor(Math.random() * players.size())));
        }
        return randomPlayers;
    }
}
