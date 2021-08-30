package models.config;

public class StructureStopCriteriaConfig extends StopCriteriaConfig {
    private final Double percentage;

    public StructureStopCriteriaConfig(Integer parameter, Double percentage) {
        super(StopCriteriaConfig.StopCriteriaType.STRUCTURE, parameter);
        this.percentage = percentage;
    }

    public Double getPercentage() {
        return this.percentage;
    }
}
