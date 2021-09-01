package geneticAlgorithm.geneticOperators.crossover;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.concurrent.ThreadLocalRandom;

public class AnnularCrossover extends Crossover {
    @Override
    public Player[] cross(Player p1, Player p2) {
        int point1 = ThreadLocalRandom.current().nextInt(Gene.values().length - 1);
        int length = ThreadLocalRandom.current().nextInt(Gene.values().length / 2);
        int point2 = (point1 + length) % Gene.values().length;
        int start, end;
        boolean swapPlayers;
        if(point1 > point2) {
            end = point1;
            start = point2;
            swapPlayers = true;
        } else {
            end = point2;
            start = point1;
            swapPlayers = false;
        }
        if (swapPlayers){
            return performSwap(Gene.getGenes(start, end), p2, p1);
        } else {
            return performSwap(Gene.getGenes(start, end), p1, p2);
        }
    }
}
