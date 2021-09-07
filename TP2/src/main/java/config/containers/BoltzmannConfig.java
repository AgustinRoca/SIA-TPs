package config.containers;

public class BoltzmannConfig {
    private final double k;
    private final double t0;
    private final double tc;

    public BoltzmannConfig(double k, double t0, double tc) {
        this.k = k;
        this.t0 = t0;
        this.tc = tc;
    }

    public double getK() {
        return k;
    }

    public double getT0() {
        return t0;
    }

    public double getTc() {
        return tc;
    }
}
