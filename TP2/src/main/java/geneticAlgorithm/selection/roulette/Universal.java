package geneticAlgorithm.selection.roulette;

public class Universal extends Roulette {
    private final double random = Math.random();

    @Override
    double randomGenerator(int i, int k) {
        return (random + i)/k;
    }
}
