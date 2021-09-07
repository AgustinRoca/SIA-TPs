package config.containers;

public class BoltzmannConfig {
    private final double k;

    public BoltzmannConfig(double k) {
        this.k = k;
    }

    public double getK() {
        return k;
    }
}
