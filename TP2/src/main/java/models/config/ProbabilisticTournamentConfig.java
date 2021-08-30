package models.config;

public class ProbabilisticTournamentConfig {
    private final double probability;
    private final int window;

    public ProbabilisticTournamentConfig(double probability, int window) {
        this.probability = probability;
        this.window = window;
    }

    public double getProbability() {
        return this.probability;
    }

    public int getWindow() {
        return this.window;
    }
}
