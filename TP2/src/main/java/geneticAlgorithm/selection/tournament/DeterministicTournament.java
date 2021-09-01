package geneticAlgorithm.selection.tournament;

import models.player.Player;

import java.util.Collection;

public class DeterministicTournament extends Tournament {
    public DeterministicTournament(int playersInMatch) {
        super(playersInMatch);
    }

    @Override
    Player getWinner(Collection<Player> players){
        Player winner = null;
        for (Player player : players){
            if (winner == null || winner.fitness() < player.fitness()) {
                winner = player;
            }
        }
        return winner;
    }
}
