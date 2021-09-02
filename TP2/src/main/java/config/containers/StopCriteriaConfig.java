package config.containers;

public class StopCriteriaConfig {
    private final StopCriteriaType type;
    private final Number parameter;
    private final double percentage;

    public StopCriteriaConfig(StopCriteriaType type, Number parameter, double percentage) {
        this.type = type;
        this.parameter = parameter;
        this.percentage = percentage;
    }

    public StopCriteriaType getType() {
        return this.type;
    }

    public Number getParameter() {
        return this.parameter;
    }

    public double getPercentage() {
        return percentage;
    }

    public enum StopCriteriaType {
        GENERATIONS,
        TIMEOUT,
        ACCEPTABLE_SOLUTION,
        CONTENT,
        STRUCTURE
    }
}
