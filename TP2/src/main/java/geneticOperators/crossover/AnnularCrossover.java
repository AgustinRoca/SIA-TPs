package geneticOperators.crossover;

import geneticOperators.Gene;
import models.player.Player;

public class AnnularCrossover extends Crossover {
    @Override
    public Player[] cross(Player p1, Player p2) {
        int start = (int) (Math.random() * (Gene.values().length - 1));
        int end = (int) (Math.random() * (Gene.values().length - start) + start);

        return performSwap(Gene.getGenes(start, end), p1, p2);
    }
}
