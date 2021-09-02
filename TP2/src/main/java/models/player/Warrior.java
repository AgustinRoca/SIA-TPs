package models.player;

import models.equipment.*;

import java.util.Map;

public class Warrior extends Player {
    public Warrior(double height, Map<Class<? extends Equipment>, Equipment> equipments) {
        super(height, equipments);
    }

    public Warrior(double height, Boots boots, Gloves gloves, Helmet helmet, Vest vest, Weapon weapon) {
        super(height, boots, gloves, helmet, vest, weapon);
    }

    @Override
    protected double calculateFitness() {
        return 0.6 * (this.attackPoints() + this.defensePoints());
    }

    @Override
    public Class<Warrior> getPlayerType() {
        return Warrior.class;
    }
}
