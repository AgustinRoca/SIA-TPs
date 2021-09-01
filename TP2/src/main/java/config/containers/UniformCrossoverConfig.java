package config.containers;

public class UniformCrossoverConfig extends CrossoverConfig {
    private final double probability;

    public UniformCrossoverConfig(double probability) {
        super(CrossoverType.UNIFORM);
        this.probability = probability;
    }

    public double getProbability() {
        return this.probability;
    }
}
