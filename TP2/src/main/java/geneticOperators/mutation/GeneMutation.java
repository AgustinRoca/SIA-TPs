package geneticOperators.mutation;

import geneticOperators.Gene;
import models.player.Player;

public class GeneMutation extends Mutation{
    public GeneMutation(double mutationProbability, boolean randomHeightMutation) {
        super(mutationProbability, randomHeightMutation);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        double probability = Math.random();
        if(probability < mutationProbability) {
            int geneToMutate = (int) Math.floor(Math.random() * Gene.values().length);
            mutateGene(Gene.values()[geneToMutate], newPlayer);
        }
        return newPlayer;
    }
}
