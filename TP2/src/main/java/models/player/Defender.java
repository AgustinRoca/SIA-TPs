package models.player;

import models.equipment.*;

import java.util.Map;

public class Defender extends Player {
    private static final double OPTIMAL_HEIGHT = 1.625;

    public Defender(Map<Class<? extends Equipment>, Equipment> equipments) {
        super(OPTIMAL_HEIGHT, equipments);
    }

    public Defender(double height, Map<Class<? extends Equipment>, Equipment> equipments) {
        super(height, equipments);
    }

    public Defender(double height, Boots boots, Gloves gloves, Helmet helmet, Vest vest, Weapon weapon) {
        super(height, boots, gloves, helmet, vest, weapon);
    }

    @Override
    protected double calculateFitness() {
        return 0.3 * this.attackPoints() + 0.8 * this.defensePoints();
    }

    @Override
    public double getOptimalHeight() {
        return 1.625;
    }

    @Override
    public Class<Defender> getPlayerType() {
        return Defender.class;
    }
}
