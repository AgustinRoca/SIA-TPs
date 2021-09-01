package selection.tournament;

import models.player.Player;
import selection.SelectionMethod;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

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
