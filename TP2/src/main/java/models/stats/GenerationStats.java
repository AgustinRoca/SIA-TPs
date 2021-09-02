package models.stats;

import models.equipment.*;
import models.player.Player;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static models.player.Player.MIN_HEIGHT;

public class GenerationStats {
    private static final int HEIGHT_THRESHOLD_MM = 1;
    private static final int DECIMALS = 5;
    private static final int MIN_HEIGHT_MM = (int) Math.floor(MIN_HEIGHT*Math.pow(10, DECIMALS));

    private final double min;
    private final double max;
    private final double avg;
    private final double median;
    private final GenerationDiversity diversity;

    private GenerationStats(double min, double max, double avg, double median, GenerationDiversity diversity) {
        this.min = min;
        this.max = max;
        this.avg = avg;
        this.median = median;
        this.diversity = diversity;
    }

    public double getMin() {
        return this.min;
    }

    public double getMax() {
        return this.max;
    }

    public double getAvg() {
        return this.avg;
    }

    public double getMedian() {
        return this.median;
    }

    public GenerationDiversity getDiversity() {
        return this.diversity;
    }

    /**
     * @param generation is a descending sorted list via each player's fitness. lastGeneration[0] is the player with max fitness
     */
    public static GenerationStats from(List<Player> generation) {
        Set<Boots> boots = new HashSet<>();
        Set<Gloves> gloves = new HashSet<>();
        Set<Helmet> helmets = new HashSet<>();
        Set<Vest> vests = new HashSet<>();
        Set<Weapon> weapons = new HashSet<>();
        Set<Double> heights = new HashSet<>();

        double sum = 0;
        for (Player player : generation) {
            boots.add(player.getBoots());
            gloves.add(player.getGloves());
            helmets.add(player.getHelmet());
            vests.add(player.getVest());
            weapons.add(player.getWeapon());
            heights.add(GenerationStats.height(player.getHeight()));

            sum += player.fitness();
        }

        return new GenerationStats(
                generation.get(generation.size() - 1).fitness(),
                generation.get(0).fitness(),
                sum / generation.size(),
                GenerationStats.median(generation),
                new GenerationDiversity(
                        boots.size(),
                        gloves.size(),
                        helmets.size(),
                        vests.size(),
                        weapons.size(),
                        heights.size()
                )
        );
    }

    private static double median(List<Player> generation) {
        if (generation.size() % 2 == 1) {
            return generation.get(generation.size() / 2).fitness();
        } else {
            int middle = generation.size() / 2;
            return (generation.get(middle - 1).fitness() + generation.get(middle).fitness()) / 2;
        }
    }

    private static double height(double height) {
        int heightMm = (int) Math.floor(height * Math.pow(10, DECIMALS));
        int rest = (heightMm - MIN_HEIGHT_MM) % HEIGHT_THRESHOLD_MM;
        return (heightMm - rest) / Math.pow(10, DECIMALS);
    }
}
