package models.player;

import models.equipment.*;

import java.util.Map;

public class Undercover extends Player {
    public Undercover(double height) {
        super(height);
    }

    public Undercover(double height, Map<Class<? extends Equipment>, Equipment> equipments) {
        super(height, equipments);
    }

    @Override
    public double fitness() {
        return 0.8 * this.attackPoints() + 0.3 * this.defensePoints();
    }

    @Override
    public Class<Undercover> getPlayerType() {
        return Undercover.class;
    }
}
