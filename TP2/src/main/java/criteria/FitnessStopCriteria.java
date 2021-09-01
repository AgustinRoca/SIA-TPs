package criteria;

public class FitnessStopCriteria implements StopCriteria {
    private final double minFitness;

    public FitnessStopCriteria(double minFitness) {
        this.minFitness = minFitness;
    }

    @Override
    public boolean shouldStop(StopCriteriaData data) {
        return minFitness < data.getCurrentMaxFitness();
    }
}
