package selection;

import models.player.Player;

import java.util.Collection;

public interface SelectionMethod {
    Collection<Player> select(Collection<Player> players, int k, int generation);
}
