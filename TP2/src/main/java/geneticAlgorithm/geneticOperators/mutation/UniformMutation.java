package geneticAlgorithm.geneticOperators.mutation;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.concurrent.ThreadLocalRandom;

public class UniformMutation extends Mutation {

    public UniformMutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement) {
        super(mutationProbability, randomHeightMutation, maxIncrement);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        double probability;

        for(int i = 0; i < Gene.values().length; i++) {
            probability = ThreadLocalRandom.current().nextDouble();

            if(probability < getMutationProbability())
                mutateGene(Gene.values()[i], newPlayer);
        }
        return newPlayer;
    }
}
