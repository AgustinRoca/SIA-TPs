package models.equipment;

import java.util.Comparator;
import java.util.TreeMap;

public abstract class Equipment {
    private final int id;
    private final double force;
    private final double agility;
    private final double endurance;
    private final double intelligence;
    private final double health;
    private EquipmentSkill bestSkill;

    public Equipment(int id, double force, double agility, double endurance, double intelligence, double health) {
        this.id = id;
        this.force = force;
        this.agility = agility;
        this.endurance = endurance;
        this.intelligence = intelligence;
        this.health = health;

        this.setBestSkill();
    }

    public int getId() {
        return this.id;
    }

    public double getForce() {
        return this.force;
    }

    public double getAgility() {
        return this.agility;
    }

    public double getEndurance() {
        return this.endurance;
    }

    public double getIntelligence() {
        return this.intelligence;
    }

    public double getHealth() {
        return this.health;
    }

    public EquipmentSkill getBestSkill() {
        return this.bestSkill;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || !o.getClass().equals(this.getClass())) return false;
        Equipment equipment = (Equipment) o;
        return this.getId() == equipment.getId() && Double.compare(equipment.getForce(), this.getForce()) == 0 && Double.compare(equipment.getAgility(), this.getAgility()) == 0 && Double.compare(equipment.getEndurance(), this.getEndurance()) == 0 && Double.compare(equipment.getIntelligence(), this.getIntelligence()) == 0 && Double.compare(equipment.getHealth(), this.getHealth()) == 0;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(this.getId());
    }

    @Override
    public String toString() {
        return "{id=" + id +
                ", force=" + force +
                ", agility=" + agility +
                ", endurance=" + endurance +
                ", intelligence=" + intelligence +
                ", health=" + health +
                '}';
    }

    private void setBestSkill() {
        TreeMap<Double, EquipmentSkill> map = new TreeMap<>(Comparator.reverseOrder());

        map.put(this.force, EquipmentSkill.FORCE);
        map.put(this.agility, EquipmentSkill.AGILITY);
        map.put(this.endurance, EquipmentSkill.ENDURANCE);
        map.put(this.intelligence, EquipmentSkill.INTELLIGENCE);
        map.put(this.health, EquipmentSkill.HEALTH);

        this.bestSkill = map.pollFirstEntry().getValue();
    }

    public enum EquipmentSkill {
        FORCE,
        AGILITY,
        ENDURANCE,
        INTELLIGENCE,
        HEALTH
    }
}
