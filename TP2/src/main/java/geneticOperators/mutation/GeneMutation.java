package geneticOperators.mutation;

import geneticOperators.Gene;
import models.player.Player;

public class GeneMutation extends Mutation {
    public GeneMutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement) {
        super(mutationProbability, randomHeightMutation, maxIncrement);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        int geneToMutate = (int) (Math.random() * Gene.values().length);
        double probability = Math.random();

        if(probability < getMutationProbability())
            mutateGene(Gene.values()[geneToMutate], newPlayer);
        return newPlayer;
    }
}
