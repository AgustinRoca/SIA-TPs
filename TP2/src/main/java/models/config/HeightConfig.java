package models.config;

public class HeightConfig {
    private final boolean random;
    private final double increment;

    public HeightConfig(boolean random, double increment) {
        this.random = random;
        this.increment = increment;
    }

    public boolean isRandom() {
        return this.random;
    }

    public double getIncrement() {
        return this.increment;
    }
}
