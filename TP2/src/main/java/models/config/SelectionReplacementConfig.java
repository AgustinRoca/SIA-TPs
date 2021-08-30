package models.config;

public class SelectionReplacementConfig {
    private final SelectionReplacementMethod methodA;
    private final SelectionReplacementMethod methodB;
    private final double factor;

    public SelectionReplacementConfig(SelectionReplacementMethod methodA, SelectionReplacementMethod methodB, double factor) {
        this.methodA = methodA;
        this.methodB = methodB;
        this.factor = factor;
    }

    public SelectionReplacementMethod getMethodA() {
        return this.methodA;
    }

    public SelectionReplacementMethod getMethodB() {
        return this.methodB;
    }

    public double getFactor() {
        return this.factor;
    }

    public enum SelectionReplacementMethod {
        ELITE,
        ROULETTE,
        UNIVERSAL,
        BOLTZMANN,
        TOURNAMENT_DETERMINISTIC,
        TOURNAMENT_PROBABILISTIC,
        RANKING
    }
}
