package models.player;

public class Warrior extends Player {
    public Warrior(double height) {
        super(height);
    }

    @Override
    public double fitness() {
        return 0.6 * (this.attackPoints() + this.defensePoints());
    }
}
