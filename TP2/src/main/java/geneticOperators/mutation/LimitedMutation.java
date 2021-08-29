package geneticOperators.mutation;

import geneticOperators.Gene;
import models.player.Player;

import java.util.Arrays;
import java.util.List;

public class LimitedMutation extends Mutation{
    public LimitedMutation(double mutationProbability, boolean randomHeightMutation) {
        super(mutationProbability, randomHeightMutation);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        int numberOfGenesToMutate = (int) Math.floor(Math.random() * Gene.values().length) + 1;

        List<Gene> genes = Arrays.asList(Gene.values());

        for(int i = 0; i < numberOfGenesToMutate; i++) {
            int randomGene = (int) Math.floor(Math.random() * genes.size());
            mutateGene(genes.get(randomGene), newPlayer);
            genes.remove(randomGene);
        }
        return newPlayer;
    }
}
