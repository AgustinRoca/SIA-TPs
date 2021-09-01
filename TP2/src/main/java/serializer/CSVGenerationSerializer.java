package serializer;

import models.player.Player;
import models.stats.GenerationStats;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class CSVGenerationSerializer implements GenerationSerializer {
    private static final char SEPARATOR = ';';
    private static final char NEW_LINE = '\n';
    private final FileWriter fileWriter;

    public CSVGenerationSerializer(String outputPath) throws IOException {
        this.fileWriter = new FileWriter(outputPath);

        this.writeHeader();
    }

    /**
     * @param generationCount generation count (initial should be zero)
     * @param generation is a descending sorted list via each player's fitness. lastGeneration[0] is the player with max fitness
     */
    public void serialize(int generationCount, List<Player> generation) {
        GenerationStats stats = GenerationStats.from(generation);

        this.write(String.valueOf(generationCount));
        this.write(String.valueOf(stats.getMin()));
        this.write(String.valueOf(stats.getMax()));
        this.write(String.valueOf(stats.getMedian()));
        this.write(String.valueOf(stats.getAvg()));

        this.write(String.valueOf(stats.getDiversity().getBoots()));
        this.write(String.valueOf(stats.getDiversity().getGloves()));
        this.write(String.valueOf(stats.getDiversity().getHelmets()));
        this.write(String.valueOf(stats.getDiversity().getVests()));
        this.write(String.valueOf(stats.getDiversity().getWeapons()));
        this.write(String.valueOf(stats.getDiversity().getHeights()), true);
    }

    private void writeHeader() {
        this.write("generation");
        this.write("min");
        this.write("max");
        this.write("median");
        this.write("avg");
        this.write("diversity_boots");
        this.write("diversity_gloves");
        this.write("diversity_helmet");
        this.write("diversity_vest");
        this.write("diversity_weapon");
        this.write("diversity_height", true);
    }

    private void write(String s) {
        this.write(s, false);
    }

    private void write(String s, boolean newLine) {
        try {
            this.fileWriter.write(s);
            if (newLine) {
                this.fileWriter.write(NEW_LINE);
                this.fileWriter.flush();
            } else {
                this.fileWriter.write(SEPARATOR);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
