package geneticAlgorithm.geneticOperators.mutation;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

public class CompleteMutation extends Mutation{
    public CompleteMutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement) {
        super(mutationProbability, randomHeightMutation, maxIncrement);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        double probability = Math.random();

        if(probability < getMutationProbability())
            for(int i = 0; i < Gene.values().length; i++)
                mutateGene(Gene.values()[i], newPlayer);

        return newPlayer;
    }
}
