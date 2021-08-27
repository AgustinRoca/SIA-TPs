package models.player;

public class Defender extends Player {
    public Defender(double height) {
        super(height);
    }

    @Override
    public double fitness() {
        return 0.3 * this.attackPoints() + 0.8 * this.defensePoints();
    }
}
