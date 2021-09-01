package geneticAlgorithm.geneticOperators.crossover;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.concurrent.ThreadLocalRandom;

public class TwoPointCrossover extends Crossover {
    @Override
    public Player[] cross(Player p1, Player p2) {
        int point1 = ThreadLocalRandom.current().nextInt(Gene.values().length - 1);
        int point2 = ThreadLocalRandom.current().nextInt(Gene.values().length - 1);
        int start, end;

        if(point1 > point2) {
            end = point1;
            start = point2;
        } else {
            end = point2;
            start = point1;
        }

        return performSwap(Gene.getGenes(start, end+1), p1, p2);
    }
}
