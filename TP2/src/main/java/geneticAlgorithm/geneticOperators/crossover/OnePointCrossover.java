package geneticAlgorithm.geneticOperators.crossover;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.concurrent.ThreadLocalRandom;

public class OnePointCrossover extends Crossover {
    @Override
    public Player[] cross(Player p1, Player p2) {
        int point = ThreadLocalRandom.current().nextInt(Gene.values().length);
        return performSwap(Gene.getGenes(point, Gene.values().length), p1, p2);
    }
}
