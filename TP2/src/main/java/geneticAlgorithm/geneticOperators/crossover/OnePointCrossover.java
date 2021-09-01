package geneticAlgorithm.geneticOperators.crossover;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

public class OnePointCrossover extends Crossover {
    @Override
    public Player[] cross(Player p1, Player p2) {
        int point = (int) (Math.random() * Gene.values().length);
        return performSwap(Gene.getGenes(point, Gene.values().length), p1, p2);
    }
}
