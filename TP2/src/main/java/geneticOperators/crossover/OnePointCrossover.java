package geneticOperators.crossover;

import geneticOperators.Gene;
import models.player.Player;

import java.util.List;

public class OnePointCrossover extends Crossover{
    public OnePointCrossover(double uniformCrossoverProbability) {
        super(uniformCrossoverProbability);
    }

    @Override
    public List<Player> cross(Player p1, Player p2) { // TODO: implement
        int point = (int) Math.floor(Math.random() * Gene.values().length);

//        if()
//
//        for(int i = point; i < NUMBER_OF_GENES; i++) {
//            double heightAux = p1.getHeight();
//            p1.setHeight(p2.getHeight());
//            p2.setHeight(heightAux);
//
//
//        }
        return null;
    }
}
