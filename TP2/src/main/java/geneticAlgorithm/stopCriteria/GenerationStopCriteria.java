package geneticAlgorithm.stopCriteria;

public class GenerationStopCriteria implements StopCriteria{
    private final int maxGenerations;

    public GenerationStopCriteria(int maxGenerations) {
        this.maxGenerations = maxGenerations;
    }

    @Override
    public boolean shouldStop(StopCriteriaData data) {
        return data.getGenerationsQuantity() >= maxGenerations;
    }
}
