package geneticOperators;

import models.equipment.*;
import models.player.Player;

public class Crossover extends GeneticOperator {
    double uniformCrossoverProbability;

    private void crossoverGene(int gene, Player p1, Player p2) {
        Equipment eq1Aux = null, eq2Aux = null;
        switch (gene) {
            case 0:
                double heightAux = p1.getHeight();
                p1.setHeight(p2.getHeight());
                p2.setHeight(heightAux);
                break;
            case 1:
                eq1Aux = p1.getEquipments().get(Boots.class);
                eq2Aux = p2.getEquipments().get(Boots.class);
                break;
            case 2:
                eq1Aux = p1.getEquipments().get(Gloves.class);
                eq2Aux = p2.getEquipments().get(Gloves.class);
                break;
            case 3:
                eq1Aux = p1.getEquipments().get(Helmet.class);
                eq2Aux = p2.getEquipments().get(Helmet.class);
                break;
            case 4:
                eq1Aux = p1.getEquipments().get(Vest.class);
                eq2Aux = p2.getEquipments().get(Vest.class);
                break;
            case 5:
                eq1Aux = p1.getEquipments().get(Weapon.class);
                eq2Aux = p2.getEquipments().get(Weapon.class);
                break;
        }

        if(gene > 1) {
            p1.replaceEquipment(eq2Aux);

            p2.replaceEquipment(eq1Aux);
        }
    }

    public Crossover(double uniformCrossoverProbability) {
        this.uniformCrossoverProbability = uniformCrossoverProbability;
    }

    public Player [] onePointCrossover(Player p1, Player p2) {
        int point = (int) (Math.random() * NUMBER_OF_GENES);

        return performSwap(point, NUMBER_OF_GENES, p1, p2);
    }

    public Player [] twoPointCrossover(Player p1, Player p2) {
        int point1 = (int) (Math.random() * (NUMBER_OF_GENES - 1));
        int point2 = (int) (Math.random() * (NUMBER_OF_GENES - 1));
        int start, end;

        if(point1 > point2) {
            end = point1;
            start = point2;
        } else {
            end = point2;
            start = point1;
        }

        return performSwap(start, end + 1, p1, p2);
    }

    public Player [] annularCrossover(Player p1, Player p2) {
        int start = (int) (Math.random() * (NUMBER_OF_GENES - 1));
        int end = (int) (Math.random() * (NUMBER_OF_GENES - start) + start);

        return performSwap(start, end, p1, p2);
    }

    public Player [] uniformCrossover(Player p1, Player p2) {
        Player [] newPlayers = new Player[2];
        Player newPlayer1 = copyPlayer(p1), newPlayer2 = copyPlayer(p2);
        double probability;

        for(int i = 0; i < NUMBER_OF_GENES; i++) {
            probability = Math.random();

            if(probability < uniformCrossoverProbability)
                crossoverGene(i, newPlayer1, newPlayer2);
        }

        newPlayers[0] = newPlayer1;
        newPlayers[1] = newPlayer2;

        return newPlayers;
    }

    private Player [] performSwap(int start, int end, Player p1, Player p2) {
        Player [] newPlayers = new Player[2];
        Player newPlayer1 = copyPlayer(p1), newPlayer2 = copyPlayer(p2);

        for(int i = start; i < end; i++)
            crossoverGene(i, newPlayer1, newPlayer2);

        newPlayers[0] = newPlayer1;
        newPlayers[1] = newPlayer2;

        return newPlayers;
    }
}
