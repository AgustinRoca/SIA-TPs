import models.player.Player;

import java.util.ArrayList;
import java.util.List;

public class Mutation {
    private final double mutationProbability;
    private static final int NUMBER_OF_GENES = 5;

    private void mutateGene(int gene, Player player) {
        System.out.println("Mutated gene: " + gene);    // TODO: define how each gene mutates
    }

    public Mutation(double mutationProbability) {
        this.mutationProbability = mutationProbability;
    }

    public void geneMutation(Player player) {
        int geneToMutate = (int) (Math.random() * NUMBER_OF_GENES);
        double probability = Math.random();

        if(probability < mutationProbability)
            mutateGene(geneToMutate, player);
    }

    public void limitedMutation(Player player) {
        int genesToMutate = (int) (Math.random() * (NUMBER_OF_GENES - 1) + 1);

        List<Integer> genes = new ArrayList<>();

        for(int i = 0; i < NUMBER_OF_GENES; i++)
            genes.add(i);


        for(int i = 0; i < genesToMutate; i++) {
            int randomGene = (int) (Math.random() * (NUMBER_OF_GENES - i));

            mutateGene(genes.get(randomGene), player);
            genes.remove(randomGene);
        }

    }

    public void uniformMutation(Player player) {
        double probability;

        for(int i = 0; i < NUMBER_OF_GENES; i++) {
            probability = Math.random();

            if(probability < mutationProbability)
                mutateGene(i, player);
        }
    }

    public void completeMutation(Player player) {
        double probability = Math.random();

        if(probability < mutationProbability)
            for(int i = 0; i < NUMBER_OF_GENES; i++)
                mutateGene(i, player);
    }
}
