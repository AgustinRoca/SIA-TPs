package config.containers;

public class HeightConfig {
    private final boolean random;
    private final boolean precalculated;
    private final double increment;

    public static HeightConfig precalculated() {
        return new HeightConfig(false, 0, true);
    }

    public static HeightConfig random() {
        return new HeightConfig(true, 0, false);
    }

    public static HeightConfig increment(double increment) {
        return new HeightConfig(false, increment, false);
    }

    private HeightConfig(boolean random, double increment, boolean precalculated) {
        this.random = random;
        this.increment = increment;
        this.precalculated = precalculated;
    }

    public boolean isRandom() {
        return this.random;
    }

    public double getIncrement() {
        return this.increment;
    }

    public boolean getPrecalculated() {
        return this.precalculated;
    }
}
