package models.config;

public class ProbabilisticTournamentConfig{
    private final double probability;

    public ProbabilisticTournamentConfig(double probability) {
        this.probability = probability;
    }

    public double getProbability() {
        return this.probability;
    }
}
