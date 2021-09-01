package geneticOperators.mutation;

import geneticOperators.Gene;
import models.player.*;

import java.util.ArrayList;
import java.util.List;

public abstract class Mutation {
    private final double mutationProbability;
    private final boolean randomHeightMutation;
    private final double maxIncrement;

    void mutateGene(Gene gene, Player player) {
        switch (gene) {
            case HEIGHT:
                if(randomHeightMutation)
                    player.setHeight(Player.randomHeight());
                else {
                    double increment = Math.random() * 2*maxIncrement - maxIncrement;  // (-maxIncrement, maxIncrement)
                    player.setHeight(player.getHeight() + increment);
                }
                break;
            case BOOTS: // TODO: BOOTS GENE
                break;
            case GLOVES: // TODO: GLOVES GENE
                break;
            case HELMET: // TODO: HELMET GENE
                break;
            case VEST: // TODO: VEST GENE
                break;
            case WEAPON: // TODO: WEAPON GENE
                break;
        }
    }

    public Mutation(double mutationProbability, boolean randomHeightMutation, double maxIncrement) {
        this.mutationProbability = mutationProbability;
        this.randomHeightMutation = randomHeightMutation;
        this.maxIncrement = maxIncrement;
    }

    public abstract Player mutate(Player player);

    public double getMutationProbability() {
        return mutationProbability;
    }

    public boolean isRandomHeightMutation() {
        return randomHeightMutation;
    }

    public double getMaxIncrement() {
        return maxIncrement;
    }
}
