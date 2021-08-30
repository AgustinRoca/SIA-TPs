package models.config;

public class BoltzmannConfig {
    private final double t0;
    private final double tk;

    public BoltzmannConfig(double t0, double tk) {
        this.t0 = t0;
        this.tk = tk;
    }

    public double getT0() {
        return this.t0;
    }

    public double getTk() {
        return this.tk;
    }
}
