package selection;

import models.player.Player;

import java.util.Collection;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class Elite implements SelectionMethod{
    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        List<Player> ans = new LinkedList<>();
        while(k > players.size()){
            ans.addAll(players);
            k -= players.size();
        }
        ans.addAll(players.stream().sorted().limit(k).collect(Collectors.toList()));
        return ans;
    }
}
