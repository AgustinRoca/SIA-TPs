package geneticAlgorithm.stopCriteria;

import models.player.Player;

import java.util.*;

public class StopCriteriaData {
    List<List<Player>> generations = new LinkedList<>();
    private final long startTime = System.currentTimeMillis();
    private int stableGenerations = 0;
    private int stablePercentageGenerations = 0;
    private final int quantityStable;

    public StopCriteriaData(double percentageStable, int generationSize) {
        this.quantityStable = (int) (percentageStable * generationSize);
    }

    public List<List<Player>> getGenerations() {
        return generations;
    }

    public List<Player> getLastGeneration() {
        return generations.get(generations.size()-1);
    }

    public int getGenerationsQuantity() {
        return generations.size() - 1;
    }

    public long getStartTime() {
        return startTime;
    }

    public void addGeneration(Collection<Player> generation) {
        List<Player> generationList = new ArrayList<>(generation);
        generationList.sort(Comparator.reverseOrder()); // Mayor fitness primero

        if(!generations.isEmpty()) {
            List<Player> previousGeneration = generations.get(generations.size() - 1);
            if (generationList.get(0).fitness() == previousGeneration.get(0).fitness()) {
                stableGenerations++;
            } else {
                stableGenerations = 0;
            }

            boolean stable = true;
            for (int i = 0; i < quantityStable && stable; i++) {
                stable = previousGeneration.get(i) == generationList.get(i);
            }
            if(stable){
                stablePercentageGenerations++;
            } else {
                stablePercentageGenerations = 0;
            }
        }

        generations.add(generationList);
    }

    public double getCurrentMaxFitness() {
        return generations.get(generations.size() - 1).get(0).fitness();
    }

    public int getStableGenerations() {
        return stableGenerations;
    }

    public int getStablePercentageGenerations() {
        return stablePercentageGenerations;
    }
}
