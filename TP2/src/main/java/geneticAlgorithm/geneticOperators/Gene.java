package geneticAlgorithm.geneticOperators;

import models.equipment.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public enum Gene {
    HEIGHT(null),
    BOOTS(Boots.class),
    GLOVES(Gloves.class),
    HELMET(Helmet.class),
    VEST(Vest.class),
    WEAPON(Weapon.class);

    Class<? extends Equipment> clazz;

    Gene(Class<? extends Equipment> clazz) {
        this.clazz = clazz;
    }

    public boolean isEquipment() {
        return clazz != null;
    }

    public Class<? extends Equipment> getEquipmentType() {
        return clazz;
    }

    public static Gene getRandomGene(){
        return values()[(int) (Math.random() * Gene.values().length)];
    }

    public static List<Gene> getGenes(int start, int end){
        return new ArrayList<>(Arrays.asList(values()).subList(start, end));
    }
}
