package player;

public class Undercover extends Player {
    public Undercover(double height) {
        super(height);
    }

    @Override
    public double fitness() {
        return 0.8 * this.attackPoints() + 0.3 * this.defensePoints();
    }
}
