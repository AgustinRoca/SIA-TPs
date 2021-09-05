package geneticAlgorithm.geneticOperators.mutation;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.concurrent.ThreadLocalRandom;

public class CompleteMutation extends Mutation{
    public CompleteMutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement, boolean usePrecalculated) {
        super(mutationProbability, randomHeightMutation, maxIncrement, usePrecalculated);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        double probability = ThreadLocalRandom.current().nextDouble();

        if(probability < getMutationProbability())
            for(int i = 0; i < Gene.values().length; i++)
                mutateGene(Gene.values()[i], newPlayer);

        return newPlayer;
    }
}
