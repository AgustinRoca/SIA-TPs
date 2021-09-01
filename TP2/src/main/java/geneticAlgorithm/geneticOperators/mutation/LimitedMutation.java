package geneticAlgorithm.geneticOperators.mutation;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LimitedMutation extends Mutation {
    public LimitedMutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement) {
        super(mutationProbability, randomHeightMutation, maxIncrement);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        int genesToMutate = (int) (Math.random() * (Gene.values().length - 1) + 1);

        List<Gene> genes = new ArrayList<>(Arrays.asList(Gene.values()));

        for(int i = 0; i < genesToMutate; i++) {
            int randomGene = (int) (Math.random() * (Gene.values().length - i));

            mutateGene(genes.get(randomGene), newPlayer);
            genes.remove(randomGene);
        }
        return newPlayer;
    }
}
