package models.player;

public class Archer extends Player {
    public Archer(double height) {
        super(height);
    }

    @Override
    public double fitness() {
        return 0.9 * this.attackPoints() + 0.1 * this.defensePoints();
    }
}
