package geneticAlgorithm.stopCriteria;

import models.player.Player;

import java.util.*;

public class StopCriteriaData {
    private ArrayList<Player> lastGeneration;
    private final long startTime = System.currentTimeMillis();
    private int stableGenerations = 0;
    private int stablePercentageGenerations = 0;
    private final int quantityStable;
    private int generationsQuantity = 0;

    public StopCriteriaData(double percentageStable, int generationSize) {
        this.quantityStable = (int) (percentageStable * generationSize);
    }

    public ArrayList<Player> getLastGeneration() {
        return this.lastGeneration;
    }

    public int getGenerationsQuantity() {
        return this.generationsQuantity;
    }

    public long getStartTime() {
        return this.startTime;
    }

    public void addGeneration(Collection<Player> generation) {
        ArrayList<Player> generationList = new ArrayList<>(generation);
        generationList.sort(Comparator.reverseOrder()); // Mayor fitness primero

        if (this.lastGeneration != null) {
            if (generationList.get(0).fitness() == this.lastGeneration.get(0).fitness()) {
                this.stableGenerations++;
            } else {
                this.stableGenerations = 0;
            }

            boolean stable = true;
            for (int i = 0; i < this.quantityStable && stable; i++) {
                stable = this.lastGeneration.get(i) == generationList.get(i);
            }
            if(stable){
                this.stablePercentageGenerations++;
            } else {
                this.stablePercentageGenerations = 0;
            }
        }

        this.lastGeneration = generationList;
        this.generationsQuantity++;
    }

    public double getCurrentMaxFitness() {
        return this.lastGeneration.get(0).fitness();
    }

    public int getStableGenerations() {
        return this.stableGenerations;
    }

    public int getStablePercentageGenerations() {
        return this.stablePercentageGenerations;
    }
}
