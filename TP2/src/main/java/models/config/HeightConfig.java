package models.config;

import models.player.Player;

public class HeightConfig {
    private final boolean random;
    private final double min;
    private final double max;
    private final double direction;

    /**
     * Random = true
     */
    public HeightConfig() {
        this(true, 0, 0, 0);
    }

    public HeightConfig(double min, double max, double direction) {
        this(false, min, max, direction);
    }

    private HeightConfig(boolean random, double min, double max, double direction) {
        this.random = random;
        this.min = min;
        this.max = max;
        this.direction = direction;
    }

    public boolean isRandom() {
        return this.random;
    }

    public double getMin() {
        return this.min;
    }

    public double getMax() {
        return this.max;
    }

    public double getDirection() {
        return this.direction;
    }
}
