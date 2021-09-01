package serializer;

import models.player.Player;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public interface GenerationSerializer {
    /**
     * @param lastGeneration is a descending sorted list via each player's fitness. lastGeneration[0] is the player with max fitness
     */
    void serialize(int generation, List<Player> lastGeneration);
}
