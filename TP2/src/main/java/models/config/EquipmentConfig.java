package models.config;

public class EquipmentConfig {
    private final boolean inMemory;
    private final String boots;
    private final String gloves;
    private final String helmet;
    private final String vest;
    private final String weapon;

    public EquipmentConfig(boolean inMemory, String boots, String gloves, String helmet, String vest, String weapon) {
        this.inMemory = inMemory;
        this.boots = boots;
        this.gloves = gloves;
        this.helmet = helmet;
        this.vest = vest;
        this.weapon = weapon;
    }

    public boolean isInMemory() {
        return this.inMemory;
    }

    public String getBoots() {
        return this.boots;
    }

    public String getGloves() {
        return this.gloves;
    }

    public String getHelmet() {
        return this.helmet;
    }

    public String getVest() {
        return this.vest;
    }

    public String getWeapon() {
        return this.weapon;
    }
}
