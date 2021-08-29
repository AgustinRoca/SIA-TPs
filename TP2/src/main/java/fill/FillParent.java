package fill;

import models.player.Player;
import selection.SelectionMethod;
import selection.Selector;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class FillParent {
    private final Selector kSelector;
    private final Selector nMinusKSelector;

    public FillParent(SelectionMethod method1, SelectionMethod method2, double a, int k, int generationSize) {
        this.kSelector = new Selector(method1, method2, a, k);
        this.nMinusKSelector = new Selector(method1, method2, a, generationSize);
    }

    public Collection<Player> getGeneration(Collection<Player> previousGeneration, Collection<Player> children, int newGenerationNumber) {
        if (children.size() > previousGeneration.size()){
            return kSelector.select(children, newGenerationNumber);
        } else {
            List<Player> newGeneration = new ArrayList<>(children);
            newGeneration.addAll(nMinusKSelector.select(previousGeneration, newGenerationNumber));
            return newGeneration;
        }
    }
}
