package selection;

import models.player.Player;

import java.util.Collection;
import java.util.stream.Collectors;

public class Elite implements SelectionMethod{
    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        return players.stream().sorted().limit(k).collect(Collectors.toList());
    }
}
