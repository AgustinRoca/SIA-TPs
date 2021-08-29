package models.player;

import models.equipment.*;

import java.util.Map;

public class Defender extends Player {
    public Defender(double height, Boots boots, Gloves gloves, Helmet helmet, Vest vest, Weapon weapon) {
        super(height, boots, gloves, helmet, vest, weapon);
    }

    public Defender(double height, Map<Class<? extends Equipment>, Equipment> equipments) {
        super(height, equipments);
    }

    @Override
    public double fitness() {
        return 0.3 * this.attackPoints() + 0.8 * this.defensePoints();
    }

    @Override
    public Class<Defender> getPlayerType() {
        return Defender.class;
    }
}
