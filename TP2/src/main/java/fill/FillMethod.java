package fill;

import models.player.Player;

import java.util.Collection;

public interface FillMethod {
    Collection<Player> getGeneration(Collection<Player> previousGeneration, Collection<Player> children, int newGenerationNumber);
}
