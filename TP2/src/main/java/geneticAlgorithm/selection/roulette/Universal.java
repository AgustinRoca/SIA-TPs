package geneticAlgorithm.selection.roulette;

import java.util.concurrent.ThreadLocalRandom;

public class Universal extends Roulette {
    private final double random = ThreadLocalRandom.current().nextDouble();

    @Override
    double randomGenerator(int i, int k) {
        return (random + i)/k;
    }
}
