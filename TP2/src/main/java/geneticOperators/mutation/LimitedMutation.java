package geneticOperators.mutation;

import geneticOperators.Gene;
import models.player.Player;

import java.util.ArrayList;
import java.util.List;

public class LimitedMutation extends Mutation {
    public LimitedMutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement) {
        super(mutationProbability, randomHeightMutation, maxIncrement);
    }

    @Override
    public Player mutate(Player player) {
        Player newPlayer = player.clone();
        int genesToMutate = (int) (Math.random() * (Gene.values().length - 1) + 1);

        List<Integer> genes = new ArrayList<>();

        for(int i = 0; i < Gene.values().length; i++)
            genes.add(i);

        for(int i = 0; i < genesToMutate; i++) {
            int randomGene = (int) (Math.random() * (Gene.values().length - i));

            mutateGene(Gene.values()[genes.get(randomGene)], newPlayer);
            genes.remove(randomGene);
        }
        return newPlayer;
    }
}
