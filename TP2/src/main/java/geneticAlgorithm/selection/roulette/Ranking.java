package geneticAlgorithm.selection.roulette;

import models.player.Player;

import java.util.ArrayList;

public class Ranking extends Roulette{
    @Override
    double aptitude(int i, ArrayList<Player> players, int generation) {
        return (players.size() - (i + 1)) / ((double) players.size());
    }
}
