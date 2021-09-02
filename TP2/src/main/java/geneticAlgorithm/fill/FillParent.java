package geneticAlgorithm.fill;

import models.player.Player;
import geneticAlgorithm.selection.SelectionMethod;
import geneticAlgorithm.selection.Selector;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class FillParent implements FillMethod {
    private final Selector kSelector;
    private final Selector nMinusKSelector;
    private final int childrenSize;
    private final int generationSize;

    public FillParent(SelectionMethod method1, SelectionMethod method2, double a, int childrenSize, int generationSize) {
        this.kSelector = new Selector(method1, method2, a, childrenSize);
        this.nMinusKSelector = new Selector(method1, method2, a, generationSize - childrenSize);
        this.generationSize = generationSize;
        this.childrenSize = childrenSize;
    }

    public Collection<Player> getGeneration(Collection<Player> previousGeneration, Collection<Player> children, int newGenerationNumber) {
        if (childrenSize >= generationSize){
            return kSelector.select(children, newGenerationNumber);
        } else {
            List<Player> newGeneration = new ArrayList<>(this.childrenSize);
            newGeneration.addAll(children);
            newGeneration.addAll(nMinusKSelector.select(previousGeneration, newGenerationNumber));
            return newGeneration;
        }
    }
}
