package geneticAlgorithm.stopCriteria;

public class PercentageStableStopCriteria implements StopCriteria {
    private final int maxStableGenerations;

    public PercentageStableStopCriteria(int maxStableGenerations) {
        this.maxStableGenerations = maxStableGenerations;
    }

    @Override
    public boolean shouldStop(StopCriteriaData data) {
        return data.getStablePercentageGenerations() >= maxStableGenerations;
    }
}
