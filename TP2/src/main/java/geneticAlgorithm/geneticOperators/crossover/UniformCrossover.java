package geneticAlgorithm.geneticOperators.crossover;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.ArrayList;
import java.util.List;

public class UniformCrossover extends Crossover{
    private final double uniformCrossoverProbability;

    public UniformCrossover(double uniformCrossoverProbability) {
        this.uniformCrossoverProbability = uniformCrossoverProbability;
    }

    @Override
    public Player[] cross(Player p1, Player p2) {
        List<Gene> genesToMutate = new ArrayList<>();
        for (Gene gene : Gene.values()) {
            if (Math.random() < uniformCrossoverProbability)
                genesToMutate.add(gene);
        }
        return performSwap(genesToMutate, p1, p2);
    }
}
