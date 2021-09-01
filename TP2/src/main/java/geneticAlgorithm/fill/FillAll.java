package geneticAlgorithm.fill;

import models.player.Player;
import geneticAlgorithm.selection.Selector;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class FillAll implements FillMethod {
    private final Selector selector;

    public FillAll(Selector selector) {
        this.selector = selector;
    }

    public Collection<Player> getGeneration(Collection<Player> previousGeneration, Collection<Player> children, int newGenerationNumber) {
        List<Player> allIndividuals = new ArrayList<>();
        allIndividuals.addAll(previousGeneration);
        allIndividuals.addAll(children);
        return selector.select(allIndividuals, newGenerationNumber);
    }
}
