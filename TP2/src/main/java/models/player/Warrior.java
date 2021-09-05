package models.player;

import models.equipment.*;

import java.util.Map;

public class Warrior extends Player {
    private static final double OPTIMAL_HEIGHT = 1.482;

    public Warrior(Map<Class<? extends Equipment>, Equipment> equipments) {
        super(OPTIMAL_HEIGHT, equipments);
    }

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
    public double getOptimalHeight() {
        return 1.482;
    }

    @Override
    public Class<Warrior> getPlayerType() {
        return Warrior.class;
    }
}
