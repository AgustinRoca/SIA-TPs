package geneticAlgorithm.geneticOperators.mutation;

import geneticAlgorithm.geneticOperators.Gene;
import models.player.Player;

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class LimitedMutation extends Mutation {
    public LimitedMutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement) {
        super(mutationProbability, randomHeightMutation, maxIncrement);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        Random random = ThreadLocalRandom.current();

        int genesToMutate = random.nextInt(Gene.values().length - 1) + 1;

        List<Gene> genes = new LinkedList<>(Arrays.asList(Gene.values()));
        Collections.shuffle(genes, random);
        for(int i = 0; i < genesToMutate; i++) {
            mutateGene(genes.remove(0), newPlayer);
        }
        return newPlayer;
    }
}
