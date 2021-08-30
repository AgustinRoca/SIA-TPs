package models.config;

public class StopCriteriaConfig {
    private final StopCriteriaType type;
    private final Number parameter;

    public StopCriteriaConfig(StopCriteriaType type, Number parameter) {
        this.type = type;
        this.parameter = parameter;
    }

    public StopCriteriaType getType() {
        return this.type;
    }

    public Number getParameter() {
        return this.parameter;
    }

    public enum StopCriteriaType {
        GENERATIONS,
        TIMEOUT,
        ACCEPTABLE_SOLUTION,
        CONTENT,
        STRUCTURE
    }
}
