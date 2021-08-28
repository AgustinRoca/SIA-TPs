package GeneticOperators;

import models.equipment.Equipment;
import models.player.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Mutation extends GeneticOperator {
    private final double mutationProbability;
    private final boolean randomHeightMutation;

    private Player copyPlayer(Player player) {
        Player newPlayer = null;

        switch (player.getClass().toString()) {
            case "class models.player.Archer":
                newPlayer = new Archer(player.getHeight());
                break;
            case "class models.player.Defender":
                newPlayer = new Defender(player.getHeight());
                break;
            case "class models.player.Undercover":
                newPlayer = new Undercover(player.getHeight());
                break;
            case "class models.player.Warrior":
                newPlayer = new Warrior(player.getHeight());
                break;
        }

        Map<Class<? extends Equipment>, Equipment> equipments = player.getEquipments();

        for(Class<? extends Equipment> k : equipments.keySet()) {
            newPlayer.addEquipment(equipments.get(k));
        }

        return newPlayer;
    }

    private void mutateGene(int gene, Player player) {
        switch (gene) {
            case 0:
                if(randomHeightMutation)    // TODO: PARAMETRIZAR OPCION
                    player.setHeight(Math.random() * (2 - 1.3) + 1.3);
                else {
                    double direction = Math.random();
                    double increment = Math.random() * (0.1 - 0.05) + 0.05;    // TODO: PARAMETRIZAR INTERVALO

                    if(direction > 0.5)             // TODO: PARAMETRIZAR PROBABILIDAD
                        player.setHeight(player.getHeight() + increment);
                    else
                        player.setHeight(player.getHeight() - increment);
                }
                break;
        }

        System.out.println("Mutated gene: " + gene);    // TODO: define how each gene mutates
    }

    public Mutation(double mutationProbability, boolean randomHeightMutation) {    // TODO: PARAMETRIZAR OPCION
        this.mutationProbability = mutationProbability;    // TODO: PARAMETRIZAR PROBABILIDAD
        this.randomHeightMutation = randomHeightMutation;    // TODO: PARAMETRIZAR OPCION
    }

    public Player geneMutation(Player player) {
        Player newPlayer = copyPlayer(player);
        int geneToMutate = (int) (Math.random() * NUMBER_OF_GENES);
        double probability = Math.random();

        if(probability < mutationProbability)
            mutateGene(geneToMutate, newPlayer);
        return newPlayer;
    }

    public Player limitedMutation(Player player) {
        Player newPlayer = copyPlayer(player);
        int genesToMutate = (int) (Math.random() * (NUMBER_OF_GENES - 1) + 1);

        List<Integer> genes = new ArrayList<>();

        for(int i = 0; i < NUMBER_OF_GENES; i++)
            genes.add(i);

        for(int i = 0; i < genesToMutate; i++) {
            int randomGene = (int) (Math.random() * (NUMBER_OF_GENES - i));

            mutateGene(genes.get(randomGene), newPlayer);
            genes.remove(randomGene);
        }
        return newPlayer;
    }

    public Player uniformMutation(Player player) {
        Player newPlayer = copyPlayer(player);
        double probability;

        for(int i = 0; i < NUMBER_OF_GENES; i++) {
            probability = Math.random();

            if(probability < mutationProbability)
                mutateGene(i, newPlayer);
        }
        return newPlayer;
    }

    public Player completeMutation(Player player) {
        Player newPlayer = copyPlayer(player);
        double probability = Math.random();

        if(probability < mutationProbability)
            for(int i = 0; i < NUMBER_OF_GENES; i++)
                mutateGene(i, newPlayer);

        return newPlayer;
    }
}
