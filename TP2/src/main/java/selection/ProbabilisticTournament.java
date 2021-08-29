package selection;

import models.player.Player;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class ProbabilisticTournament implements SelectionMethod{
    private final double threshold;

    public ProbabilisticTournament(double threshold) {
        this.threshold = threshold;
    }

    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        List<Player> playerList = new ArrayList<>(players);
        List<Player> selected = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            List<Player> randomPlayers = getRandomPlayers(playerList);
            Player player1 = randomPlayers.get(0);
            Player player2 = randomPlayers.get(1);
            Player winner;
            if (Math.random() < threshold) {
                winner = (player1.fitness() < player2.fitness()) ? player2 : player1;
            } else {
                winner = (player1.fitness() < player2.fitness()) ? player1 : player2;
            }
            selected.add(winner);
        }
        return selected;
    }

    private List<Player> getRandomPlayers(List<Player> players){
        List<Player> copyList = new ArrayList<>(players);
        List<Player> randomPlayers = new ArrayList<>();
        for (int i = 0; i < 2; i++) {
            Player randomPlayer = copyList.get((int) Math.floor(Math.random() * copyList.size()));
            randomPlayers.add(randomPlayer);
            copyList.remove(randomPlayer);
        }
        return randomPlayers;
    }
}
