package geneticOperators.mutation;

import geneticOperators.Gene;
import models.player.Player;

public class UniformMutation extends Mutation{
    public UniformMutation(double mutationProbability, boolean randomHeightMutation) {
        super(mutationProbability, randomHeightMutation);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        for(Gene gene : Gene.values()) {
            double probability = Math.random();
            if(probability < mutationProbability)
                mutateGene(gene, newPlayer);
        }
        return newPlayer;
    }
}
