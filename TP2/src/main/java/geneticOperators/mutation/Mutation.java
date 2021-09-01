package geneticOperators.mutation;

import geneticOperators.Gene;
import models.equipment.*;
import models.equipment.equipment_collection.EquipmentCollection;
import models.equipment.equipment_collection.Equipments;
import models.player.*;

import java.util.ArrayList;
import java.util.List;

public abstract class Mutation {
    private final double mutationProbability;
    private final boolean randomHeightMutation;
    private final double maxIncrement;
    private final EquipmentCollection equipments = Equipments.getInstance();


    void mutateGene(Gene gene, Player player) {
        switch (gene) {
            case HEIGHT:
                if(randomHeightMutation)
                    player.setHeight(Player.normalRandomHeight(player.getHeight()));
                else {
                    double increment = Math.random() * 2*maxIncrement - maxIncrement;  // (-maxIncrement, maxIncrement)
                    player.setHeight(player.getHeight() + increment);
                }
                break;
            case BOOTS:
                player.replaceEquipment(equipments.getEquipment(Boots.class));
                break;
            case GLOVES:
                player.replaceEquipment(equipments.getEquipment(Gloves.class));
                break;
            case HELMET:
                player.replaceEquipment(equipments.getEquipment(Helmet.class));
                break;
            case VEST:
                player.replaceEquipment(equipments.getEquipment(Vest.class));
                break;
            case WEAPON:
                player.replaceEquipment(equipments.getEquipment(Weapon.class));
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
}
