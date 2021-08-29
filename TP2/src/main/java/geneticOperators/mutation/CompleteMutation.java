package geneticOperators.mutation;

import geneticOperators.Gene;
import models.player.Player;

public class CompleteMutation extends Mutation{
    public CompleteMutation(double mutationProbability, boolean randomHeightMutation) {
        super(mutationProbability, randomHeightMutation);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        double probability = Math.random();
        if(probability < mutationProbability)
            for(Gene gene : Gene.values())
                mutateGene(gene, newPlayer);
        return newPlayer;
    }
}
