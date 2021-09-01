package config.containers;

public class CrossoverConfig {
    private final CrossoverType type;

    public CrossoverConfig(CrossoverType type) {
        this.type = type;
    }

    public CrossoverType getType() {
        return this.type;
    }

    public enum CrossoverType {
        SINGLE_POINT,
        TWO_POINTS,
        ANNULAR,
        UNIFORM
    }
}
