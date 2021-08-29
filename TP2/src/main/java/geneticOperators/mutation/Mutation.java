package geneticOperators.mutation;

import geneticOperators.Gene;
import models.player.*;

public abstract class Mutation {
    final double mutationProbability;
    final boolean randomHeightMutation;

    void mutateGene(Gene gene, Player player) {

        switch (gene) {
            case HEIGHT:
                if(randomHeightMutation)    // TODO: PARAMETRIZAR OPCION
                    player.setHeight(Math.random() * (Player.MAX_HEIGHT - Player.MIN_HEIGHT) + Player.MIN_HEIGHT);
                else {
                    double direction = Math.random();
                    double increment = Math.random() * (0.1 - 0.05) + 0.05;    // TODO: PARAMETRIZAR INTERVALO

                    if(direction > 0.5)             // TODO: PARAMETRIZAR PROBABILIDAD
                        player.setHeight(player.getHeight() + increment);
                    else
                        player.setHeight(player.getHeight() - increment);
                }
                break;
            case BOOTS:
                break;
            case GLOVES:
                break;
            case HELMET:
                break;
            case VEST:
                break;
            case WEAPON:
                break;
        }
    }

    public Mutation(double mutationProbability, boolean randomHeightMutation) {    // TODO: PARAMETRIZAR OPCION
        this.mutationProbability = mutationProbability;    // TODO: PARAMETRIZAR PROBABILIDAD
        this.randomHeightMutation = randomHeightMutation;    // TODO: PARAMETRIZAR OPCION
    }

    public abstract Player mutate(Player player);
}
