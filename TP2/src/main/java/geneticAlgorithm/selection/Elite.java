package geneticAlgorithm.selection;

import models.player.Player;

import java.util.*;

public class Elite implements SelectionMethod{
    @Override
    public Collection<Player> select(Collection<Player> players, int k, int generation) {
        List<Player> playersList = new ArrayList<>(players);
        playersList.sort(Comparator.reverseOrder());
        List<Player> ans = new LinkedList<>();
        for (int i = 0; i < playersList.size(); i++) {
            int times = (int) Math.ceil((double) (k - i)/ playersList.size());
            for (int j = 0; j < times; j++) {
                ans.add(playersList.get(i));
            }
        }
        return ans;
    }
}
