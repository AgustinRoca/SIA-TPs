package criteria;

public class StableStopCriteria implements StopCriteria {
    private final int maxStableGenerations;

    public StableStopCriteria(int maxStableGenerations) {
        this.maxStableGenerations = maxStableGenerations;
    }

    @Override
    public boolean shouldStop(StopCriteriaData data) {
        return data.getStableGenerations() >= maxStableGenerations;
    }
}
