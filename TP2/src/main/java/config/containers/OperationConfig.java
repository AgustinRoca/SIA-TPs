package config.containers;

public class OperationConfig {
    private final OperationConfig.OperationType type;

    public OperationConfig(OperationConfig.OperationType type) {
        this.type = type;
    }

    public OperationConfig.OperationType getType() {
        return this.type;
    }

    public enum OperationType {
        MUTATION,
        CROSSOVER
    }
}
