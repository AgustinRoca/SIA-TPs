package geneticOperators.crossover;

import geneticOperators.Gene;
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
        Player[] newPlayers = new Player[2];
        Player newPlayer1 = p1.clone(), newPlayer2 = p2.clone();
        double probability;

        List<Gene> genesToMutate = new ArrayList<>();
        for (Gene gene : Gene.values()) {
            probability = Math.random();
            if (probability < uniformCrossoverProbability)
                genesToMutate.add(gene);
        }
        performSwap(genesToMutate, newPlayer1, newPlayer2);

        newPlayers[0] = newPlayer1;
        newPlayers[1] = newPlayer2;

        return newPlayers;
    }
}
