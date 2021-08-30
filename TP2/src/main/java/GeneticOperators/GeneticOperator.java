package GeneticOperators;

import models.equipment.Equipment;
import models.player.*;

import java.util.Map;

public abstract class GeneticOperator {
    public static final int NUMBER_OF_GENES = 6;

    public Player copyPlayer(Player player) {
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

        for(Equipment e : equipments.values()) {
            newPlayer.replaceEquipment(e);
        }

        return newPlayer;
    }
}
