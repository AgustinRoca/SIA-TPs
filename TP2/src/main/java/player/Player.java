package player;

import equipment.Equipment;

import java.util.HashSet;
import java.util.Set;

public abstract class Player {
    private final Set<Equipment> equipments = new HashSet<>();
    private double height;

    private boolean attackPointsCalculated = false;
    private double attackPoints;
    private double attackModifier;

    private boolean defensePointsCalculated = false;
    private double defensePoints;
    private double defenseModifier;

    public Player(double height) {
        this.height = height;
    }

    public double getHeight() {
        return this.height;
    }

    public void setHeight(double height) {
        this.height = height;
        this.calculateAttackModifier();
        this.calculateDefenseModifier();
    }

    public void addEquipment(Equipment equipment) {
        this.equipments.add(equipment);
    }

    public void removeEquipment(Equipment equipment) {
        this.equipments.remove(equipment);
    }

    public double attackPoints() {
        if (!this.attackPointsCalculated)
            this.calculateAttackPoints();
        return this.attackPoints;
    }

    public double defensePoints() {
        if (!this.defensePointsCalculated)
            this.calculateDefensePoints();
        return this.attackPoints;
    }

    public abstract double fitness();

    private void calculateAttackPoints() {
        double force = 0;
        double agility = 0;
        double intelligence = 0;

        for (Equipment equipment : this.equipments) {
            force += equipment.getForce();
            agility += equipment.getAgility();
            intelligence += equipment.getIntelligence();
        }

        force = 100 * Math.tanh(0.01 * force);
        agility = Math.tanh(0.01 * agility);
        intelligence = 0.6 * Math.tanh(0.01 * intelligence);

        this.attackPoints = (agility + intelligence) * force * this.attackModifier;
        this.attackPointsCalculated = true;
    }

    private void calculateDefensePoints() {
        double endurance = 0;
        double health = 0;
        double intelligence = 0;

        for (Equipment equipment : this.equipments) {
            endurance += equipment.getEndurance();
            health += equipment.getHealth();
            intelligence += equipment.getIntelligence();
        }

        health = 100 * Math.tanh(0.01 * health);
        endurance = Math.tanh(0.01 * endurance);
        intelligence = 0.6 * Math.tanh(0.01 * intelligence);

        this.defensePoints = (endurance + intelligence) * health * this.defenseModifier;
        this.defensePointsCalculated = true;
    }

    private void calculateAttackModifier() {
        double aux = Math.pow(3 * this.height - 5, 2);

        this.attackModifier = 0.7 - Math.pow(aux, 2) + aux + this.height / 4;
    }

    private void calculateDefenseModifier() {
        double aux = Math.pow(2.5 * this.height - 4.16, 2);

        this.defenseModifier = 1.9 + Math.pow(aux, 2) - aux - (3 * this.height) / 10;
    }
}
