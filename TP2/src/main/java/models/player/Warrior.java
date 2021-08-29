package models.player;

import models.equipment.*;

import java.util.Map;

public class Warrior extends Player {
    public Warrior(double height, Boots boots, Gloves gloves, Helmet helmet, Vest vest, Weapon weapon) {
        super(height, boots, gloves, helmet, vest, weapon);
    }

    public Warrior(double height, Map<Class<? extends Equipment>, Equipment> equipments) {
        super(height, equipments);
    }

    @Override
    public double fitness() {
        return 0.6 * (this.attackPoints() + this.defensePoints());
    }

    @Override
    public Class<Undercover> getPlayerType() {
        return Undercover.class;
    }
}
