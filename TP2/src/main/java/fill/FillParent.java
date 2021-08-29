package fill;

import models.player.Player;
import selection.Selection;
import selection.SelectionMethod;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class FillParent {
    private final Selection kSelection;
    private final Selection nMinusKSelection;

    public FillParent(SelectionMethod method1, SelectionMethod method2, double a, int k, int generationSize) {
        this.kSelection = new Selection(method1, method2, a, k);
        this.nMinusKSelection = new Selection(method1, method2, a, generationSize);
    }

    public Collection<Player> getGeneration(Collection<Player> previousGeneration, Collection<Player> children, int newGenerationNumber) {
        if (children.size() > previousGeneration.size()){
            return kSelection.select(children, newGenerationNumber);
        } else {
            List<Player> newGeneration = new ArrayList<>(children);
            newGeneration.addAll(nMinusKSelection.select(previousGeneration, newGenerationNumber));
            return newGeneration;
        }
    }
}
