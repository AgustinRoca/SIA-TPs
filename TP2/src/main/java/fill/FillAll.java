package fill;

import models.player.Player;
import selection.Selection;
import selection.SelectionMethod;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class FillAll {
    private final Selection selection;

    public FillAll(SelectionMethod method1, SelectionMethod method2, double a, int k) {
        this.selection = new Selection(method1, method2, a, k);
    }

    public Collection<Player> getGeneration(Collection<Player> previousGeneration, Collection<Player> children, int newGenerationNumber) {
        List<Player> allIndividuals = new ArrayList<>();
        allIndividuals.addAll(previousGeneration);
        allIndividuals.addAll(children);
        return selection.select(allIndividuals, newGenerationNumber);
    }
}
