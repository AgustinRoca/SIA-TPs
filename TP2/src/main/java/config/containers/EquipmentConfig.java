package config.containers;

import models.equipment.*;

import java.util.HashMap;
import java.util.Map;

public class EquipmentConfig {
    private final boolean inMemory;
    private final Map<Class<? extends Equipment>, String> files;
    private final Map<Class<? extends Equipment>, Integer> equipments;

    public EquipmentConfig(boolean inMemory, Map<Class<? extends Equipment>, String> files, Map<Class<? extends Equipment>, Integer> equipments) {
        this.inMemory = inMemory;
        this.files = new HashMap<>(files);
        this.equipments = new HashMap<>(equipments);
    }

    public boolean isInMemory() {
        return this.inMemory;
    }

    public Map<Class<? extends Equipment>, String> getFiles() {
        return this.files;
    }

    public Map<Class<? extends Equipment>, Integer> getEquipments() {
        return this.equipments;
    }
}
