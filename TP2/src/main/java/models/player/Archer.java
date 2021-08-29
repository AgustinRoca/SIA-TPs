package models.player;

import models.equipment.*;

import java.util.Map;

public class Archer extends Player {
    public Archer(double height) {
        super(height);
    }

    public Archer(double height, Map<Class<? extends Equipment>, Equipment> equipments) {
        super(height, equipments);
    }

        @Override
    public double fitness() {
        return 0.9 * this.attackPoints() + 0.1 * this.defensePoints();
    }

    @Override
    public Class<Archer> getPlayerType() {
        return Archer.class;
    }
}
