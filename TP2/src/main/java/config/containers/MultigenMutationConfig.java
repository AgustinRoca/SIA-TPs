package config.containers;

public class MultigenMutationConfig extends MutationConfig {
    private final int multigenLimitedM;

    public MultigenMutationConfig(MutationType type, double probability, int multigenLimitedM) {
        super(type, probability);
        this.multigenLimitedM = multigenLimitedM;
    }

    public int getMultigenLimitedM() {
        return this.multigenLimitedM;
    }
}
