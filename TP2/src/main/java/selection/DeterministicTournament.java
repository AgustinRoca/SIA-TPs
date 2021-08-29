package selection;

import models.player.Player;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class DeterministicTournament implements SelectionMethod{
    private final int playersInMatch;

    public DeterministicTournament(int playersInMatch) {
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

    private Player getWinner(Collection<Player> players){
        Player winner = null;
        for (Player player : players){
            if (winner == null || winner.fitness() < player.fitness()) {
                winner = player;
            }
        }
        return winner;
    }

    private Collection<Player> getRandomPlayers(List<Player> players, int quantity){
        List<Player> copyList = new ArrayList<>(players);
        List<Player> randomPlayers = new ArrayList<>();
        for (int i = 0; i < quantity; i++) {
            Player randomPlayer = copyList.get((int) Math.floor(Math.random() * copyList.size()));
            randomPlayers.add(randomPlayer);
            copyList.remove(randomPlayer);
        }
        return randomPlayers;
    }
}
