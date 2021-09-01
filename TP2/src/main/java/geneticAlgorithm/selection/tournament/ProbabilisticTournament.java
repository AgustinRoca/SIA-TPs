package geneticAlgorithm.selection.tournament;

import models.player.Player;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class ProbabilisticTournament extends Tournament {
    private final double threshold;

    public ProbabilisticTournament(double threshold) {
        super(2);
        this.threshold = threshold;
    }

    @Override
    Player getWinner(Collection<Player> players) {
        List<Player> playersList = new ArrayList<>(players);
        Player player1 = playersList.get(0);
        Player player2 = playersList.get(1);
        if(ThreadLocalRandom.current().nextDouble() < threshold){
            return (player1.fitness() < player2.fitness()) ? player2 : player1;
        } else {
            return (player1.fitness() < player2.fitness()) ? player1 : player2;
        }
    }
}
