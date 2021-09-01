package config.containers;

public class MutationConfig {
    private final MutationType type;
    private final double probability;

    public MutationConfig(MutationType type, double probability) {
        this.type = type;
        this.probability = probability;
    }

    public MutationType getType() {
        return this.type;
    }

    public double getProbability() {
        return this.probability;
    }

    public enum MutationType {
        COMPLETE,
        GEN,
        MULTIGEN_LIMITED,
        MULTIGEN_UNIFORM
    }
}
