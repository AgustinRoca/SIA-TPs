package geneticAlgorithm.geneticOperators.mutation;

import geneticAlgorithm.geneticOperators.Gene;
import models.equipment.*;
import config.equipmentCollection.EquipmentCollection;
import config.equipmentCollection.Equipments;
import models.player.*;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ThreadLocalRandom;

public abstract class Mutation {
    private final double mutationProbability;
    private final boolean randomHeightMutation;
    private final boolean usePrecalculated;
    private final double maxIncrement;
    private final EquipmentCollection equipments = Equipments.getInstance();

    public Mutation(
            double mutationProbability,
            boolean randomHeightMutation,
            double maxIncrement,
            boolean usePrecalculated
    ) {
        this.mutationProbability = mutationProbability;
        this.randomHeightMutation = randomHeightMutation;
        this.maxIncrement = maxIncrement;
        this.usePrecalculated = usePrecalculated;
    }

    void mutateGene(Gene gene, Player player) {
        switch (gene) {
            case HEIGHT:
                if (this.randomHeightMutation) {
                    player.setHeight(Player.normalRandomHeight(player.getHeight()));
                } else if (this.usePrecalculated) {
                    player.setHeight(player.getOptimalHeight());
                } else {
                    double increment = ThreadLocalRandom.current().nextDouble(-this.maxIncrement, this.maxIncrement);  // (-maxIncrement, maxIncrement)
                    player.setHeight(player.getHeight() + increment);
                }
                break;
            case BOOTS:
                player.replaceEquipment(this.equipments.getEquipment(Boots.class));
                break;
            case GLOVES:
                player.replaceEquipment(this.equipments.getEquipment(Gloves.class));
                break;
            case HELMET:
                player.replaceEquipment(this.equipments.getEquipment(Helmet.class));
                break;
            case VEST:
                player.replaceEquipment(this.equipments.getEquipment(Vest.class));
                break;
            case WEAPON:
                player.replaceEquipment(this.equipments.getEquipment(Weapon.class));
                break;
        }
    }

    public abstract Player mutate(Player player);

    public double getMutationProbability() {
        return this.mutationProbability;
    }
}
