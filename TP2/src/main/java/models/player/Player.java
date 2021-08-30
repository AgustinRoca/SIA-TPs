package models.player;

import models.equipment.*;

import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;
import java.util.Map;

public abstract class Player implements Comparable<Player>, Cloneable{
    private final Map<Class<? extends Equipment>, Equipment> equipments = new HashMap<>();
    private double height;

    private boolean attackPointsCalculated = false;
    private double attackPoints;
    private double attackModifier;

    private boolean defensePointsCalculated = false;
    private double defensePoints;
    private double defenseModifier;

    public static final double MIN_HEIGHT = 1.3;
    public static final double MAX_HEIGHT = 2.0;

    public Player(double height, Map<Class<? extends Equipment>, Equipment> equipments) {
        this.height = height;
        for (Class<? extends Equipment> clazz : equipments.keySet()){
            this.equipments.put(clazz, equipments.get(clazz));
        }
    }

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
        this.attackPointsCalculated = false;
        this.defensePointsCalculated = false;
    }

    public void replaceEquipment(Equipment newEquipment) {
        this.equipments.put(newEquipment.getClass(), newEquipment);
        this.attackPointsCalculated = false;
        this.defensePointsCalculated = false;
    }

    public Boots getBoots(){
        return (Boots) equipments.get(Boots.class);
    }

    public Gloves getGloves(){
        return (Gloves) equipments.get(Gloves.class);
    }

    public Helmet getHelmet(){
        return (Helmet) equipments.get(Helmet.class);
    }

    public Vest getVest(){
        return (Vest) equipments.get(Vest.class);
    }

    public Weapon getWeapon(){
        return (Weapon) equipments.get(Weapon.class);
    }


    public abstract Class<? extends Player> getPlayerType();

    public abstract double fitness();

    public double attackPoints() {
        if (!this.attackPointsCalculated)
            this.calculateAttackPoints();
        return this.attackPoints;
    }

    public double defensePoints() {
        if (!this.defensePointsCalculated)
            this.calculateDefensePoints();
        return this.defensePoints;
    }

    public Map<Class<? extends Equipment>, Equipment> getEquipments() {
        return this.equipments;
    }

    @Override
    public int compareTo(Player o) {
        return Double.compare(fitness(), o.fitness());
    }

    public Player clone() {
        try {
            return getPlayerType()
                    .getConstructor(double.class, Boots.class, Gloves.class, Helmet.class, Vest.class, Weapon.class)
                    .newInstance(height, getBoots(), getGloves(), getHelmet(), getVest(), getWeapon());
        } catch (InstantiationException | InvocationTargetException | NoSuchMethodException | IllegalAccessException e) {
            try {
                super.clone();
            } catch (CloneNotSupportedException ex) {
                ex.printStackTrace();
            }
        }
        return null;
    }

    private void calculateAttackPoints() {
        double force = 0;
        double agility = 0;
        double intelligence = 0;

        for (Equipment equipment : this.equipments.values()) {
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

        for (Equipment equipment : this.equipments.values()) {
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
