package models.stats;

public class GenerationEquipmentFraction {
    private final double force;
    private final double agility;
    private final double endurance;
    private final double expertise;
    private final double health;

    public GenerationEquipmentFraction(double force, double agility, double endurance, double expertise, double health) {
        this.force = force;
        this.agility = agility;
        this.endurance = endurance;
        this.expertise = expertise;
        this.health = health;
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

    public double getExpertise() {
        return this.expertise;
    }

    public double getHealth() {
        return this.health;
    }
}
