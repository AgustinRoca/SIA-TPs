package equipment;

public abstract class Equipment {
    private final int id;
    private final double force;
    private final double agility;
    private final double endurance;
    private final double intelligence;
    private final double health;

    public Equipment(int id, double force, double agility, double endurance, double intelligence, double health) {
        this.id = id;
        this.force = force;
        this.agility = agility;
        this.endurance = endurance;
        this.intelligence = intelligence;
        this.health = health;
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
}
