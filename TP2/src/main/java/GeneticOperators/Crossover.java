package GeneticOperators;

import models.equipment.Equipment;
import models.player.Player;

import java.util.Map;

public class Crossover extends GeneticOperator {
    double uniformCrossoverProbability;

    public Crossover(double uniformCrossoverProbability) {
        this.uniformCrossoverProbability = uniformCrossoverProbability;
    }

    public void onePointCrossover(Player p1, Player p2) {
        int point = (int) (Math.random() * NUMBER_OF_GENES);

//        if()

//        for(int i = point; i < NUMBER_OF_GENES; i++) {
//            double heightAux = p1.getHeight();
//            p1.setHeight(p2.getHeight());
//            p2.setHeight(heightAux);
//
//
//        }
    }

    public void twoPointCrossover() {

    }

    public void annularCrossover() {

    }

    public void uniformCrossover(Player p1, Player p2) {
        double probability = Math.random();
        Map<Class<? extends Equipment>, Equipment> equipments1Aux = p1.getEquipments();
        Map<Class<? extends Equipment>, Equipment> equipments2Aux = p1.getEquipments();
        Equipment eq1;
        Equipment eq2;

        if(probability < uniformCrossoverProbability) {
            double heightAux = p1.getHeight();
            p1.setHeight(p2.getHeight());
            p2.setHeight(heightAux);
        }

        for(Class<? extends Equipment> k : equipments1Aux.keySet()) {
            probability = Math.random();

            if(probability < uniformCrossoverProbability) {
                eq1 = equipments1Aux.get(k);
                eq2 = equipments2Aux.get(k);

                p1.removeEquipment(eq1);
                p1.addEquipment(eq2);
            }
        }

    }
}
