package models.player;

import models.equipment.*;

import java.util.Map;

public class Archer extends Player {
    public Archer(double height, Map<Class<? extends Equipment>, Equipment> equipments) {
        super(height, equipments);
    }

    public Archer(double height, Boots boots, Gloves gloves, Helmet helmet, Vest vest, Weapon weapon) {
        super(height, boots, gloves, helmet, vest, weapon);
    }

    @Override
    protected double calculateFitness() {
        return 0.9 * this.attackPoints() + 0.1 * this.defensePoints();
    }

    @Override
    public Class<Archer> getPlayerType() {
        return Archer.class;
    }
}
