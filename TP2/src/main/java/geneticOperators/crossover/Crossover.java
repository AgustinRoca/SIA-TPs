package geneticOperators.crossover;

import models.player.Player;

import java.util.List;


public abstract class Crossover {
    double uniformCrossoverProbability;

    public Crossover(double uniformCrossoverProbability) {
        this.uniformCrossoverProbability = uniformCrossoverProbability;
    }

    public abstract List<Player> cross(Player p1, Player p2);
}
