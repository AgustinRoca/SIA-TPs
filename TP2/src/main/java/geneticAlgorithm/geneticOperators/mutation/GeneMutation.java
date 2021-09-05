package geneticAlgorithm.geneticOperators.mutation;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.concurrent.ThreadLocalRandom;

public class GeneMutation extends Mutation {
    public GeneMutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement, boolean usePrecalculated) {
        super(mutationProbability, randomHeightMutation, maxIncrement, usePrecalculated);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        int geneToMutate = ThreadLocalRandom.current().nextInt(Gene.values().length);
        double probability = ThreadLocalRandom.current().nextDouble();

        if(probability < getMutationProbability())
            mutateGene(Gene.values()[geneToMutate], newPlayer);
        return newPlayer;
    }
}
