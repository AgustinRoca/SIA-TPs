package models.player;

import models.equipment.*;

import java.util.Map;

public class Archer extends Player {
    private static final double OPTIMAL_HEIGHT = 1.906;

    public Archer(Map<Class<? extends Equipment>, Equipment> equipments) {
        super(OPTIMAL_HEIGHT, equipments);
    }

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
    public double getOptimalHeight() {
        return OPTIMAL_HEIGHT;
    }

    @Override
    public Class<Archer> getPlayerType() {
        return Archer.class;
    }
}
