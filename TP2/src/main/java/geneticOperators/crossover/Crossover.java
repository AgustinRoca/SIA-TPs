package geneticOperators.crossover;

import geneticOperators.Gene;
import models.equipment.*;
import models.player.Player;

import java.util.List;

public abstract class Crossover {

    public abstract Player[] cross(Player p1, Player p2);

    Player [] performSwap(List<Gene> genes, Player p1, Player p2) {
        Player [] newPlayers = new Player[2];
        Player newPlayer1 = p1.clone(), newPlayer2 = p2.clone();

        for(Gene gene : genes)
            swapGene(gene, newPlayer1, newPlayer2);

        newPlayers[0] = newPlayer1;
        newPlayers[1] = newPlayer2;

        return newPlayers;
    }

    private void swapGene(Gene gene, Player p1, Player p2) {
        if (gene == Gene.HEIGHT) {
            double heightAux = p1.getHeight();
            p1.setHeight(p2.getHeight());
            p2.setHeight(heightAux);
        } else {
            Equipment p1EquipmentAux = p1.getEquipments().get(gene.getEquipmentType());
            Equipment p2EquipmentAux = p2.getEquipments().get(gene.getEquipmentType());
            p1.replaceEquipment(gene.getEquipmentType(), p1EquipmentAux);
            p2.replaceEquipment(gene.getEquipmentType(), p2EquipmentAux);
        }
    }
}
