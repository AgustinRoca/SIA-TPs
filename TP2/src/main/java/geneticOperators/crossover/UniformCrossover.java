package geneticOperators.crossover;

import models.equipment.Equipment;
import models.player.Player;

import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UniformCrossover extends Crossover{
    public UniformCrossover(double uniformCrossoverProbability) {
        super(uniformCrossoverProbability);
    }

    @Override
    public List<Player> cross(Player p1, Player p2) {
        List<Player> children = new ArrayList<>();
        double probability = Math.random();
        double childHeight1;
        double childHeight2;
        if(probability < uniformCrossoverProbability) {
            childHeight1 = p1.getHeight();
            childHeight2 = p2.getHeight();
        } else {
            childHeight1 = p2.getHeight();
            childHeight2 = p1.getHeight();
        }

        Map<Class<? extends Equipment>, Equipment> childEquipments1 = new HashMap<>();
        Map<Class<? extends Equipment>, Equipment> childEquipments2 = new HashMap<>();
        for(Class<? extends Equipment> equipmentClazz : p1.getEquipments().keySet()) {
            probability = Math.random();
            if(probability < uniformCrossoverProbability) {
                childEquipments1.put(equipmentClazz, p1.getEquipments().get(equipmentClazz));
                childEquipments2.put(equipmentClazz, p2.getEquipments().get(equipmentClazz));
            } else {
                childEquipments1.put(equipmentClazz, p2.getEquipments().get(equipmentClazz));
                childEquipments2.put(equipmentClazz, p1.getEquipments().get(equipmentClazz));
            }
        }

        try {
            Player child1 = p1.getPlayerType()
                    .getConstructor(double.class, Map.class)
                    .newInstance(childHeight1, childEquipments1);

            Player child2 = p1.getPlayerType()
                    .getConstructor(double.class, Map.class)
                    .newInstance(childHeight2, childEquipments2);

            children.add(child1);
            children.add(child2);
        } catch (InstantiationException | IllegalAccessException | InvocationTargetException | NoSuchMethodException e) {
            e.printStackTrace();
        }

        return children;
    }
}
