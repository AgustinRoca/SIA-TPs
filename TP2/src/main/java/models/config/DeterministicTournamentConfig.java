package models.config;

public class DeterministicTournamentConfig {
    private final int playersInMatch;

    public DeterministicTournamentConfig(int playersInMatch) {
        this.playersInMatch = playersInMatch;
    }

    public int getPlayersInMatch() {
        return playersInMatch;
    }
}
