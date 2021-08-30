package models.config;

public class UniformCrossoverConfig extends CrossoverConfig {
    private final double probability;
    private final double threshold;

    public UniformCrossoverConfig(double probability, double threshold) {
        super(CrossoverType.UNIFORM);
        this.probability = probability;
        this.threshold = threshold;
    }

    public double getProbability() {
        return this.probability;
    }

    public double getThreshold() {
        return this.threshold;
    }
}
