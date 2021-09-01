package selection.roulette;

import models.player.Player;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Ranking extends Roulette{

    @Override
    double aptitude(int i, List<Player> players, int generation) {
        return (double) (players.size() - i)/players.size();
    }
}
