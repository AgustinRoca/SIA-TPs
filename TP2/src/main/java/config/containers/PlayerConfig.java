package config.containers;

import models.player.Player;

public class PlayerConfig {
    private final Class<? extends Player> playerClass;
    private final int count;
    private final int selection;
    private final HeightConfig heightConfig;

    public PlayerConfig(Class<? extends Player> playerClass, int count, int selection, HeightConfig heightConfig) {
        this.playerClass = playerClass;
        this.count = count;
        this.selection = selection;
        this.heightConfig = heightConfig;
    }

    public Class<? extends Player> getPlayerClass() {
        return this.playerClass;
    }

    public int getCount() {
        return this.count;
    }

    public int getSelection() {
        return this.selection;
    }

    public HeightConfig getHeightConfig() {
        return this.heightConfig;
    }
}
