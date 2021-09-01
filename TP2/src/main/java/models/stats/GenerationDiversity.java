package models.stats;

public class GenerationDiversity {
    private final int boots;
    private final int gloves;
    private final int helmets;
    private final int vests;
    private final int weapons;
    private final int heights;

    public GenerationDiversity(int boots, int gloves, int helmets, int vests, int weapons, int heights) {
        this.boots = boots;
        this.gloves = gloves;
        this.helmets = helmets;
        this.vests = vests;
        this.weapons = weapons;
        this.heights = heights;
    }

    public int getBoots() {
        return this.boots;
    }

    public int getGloves() {
        return this.gloves;
    }

    public int getHelmets() {
        return this.helmets;
    }

    public int getVests() {
        return this.vests;
    }

    public int getWeapons() {
        return this.weapons;
    }

    public int getHeights() {
        return this.heights;
    }
}
