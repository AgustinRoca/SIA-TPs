package config.containers;

import models.equipment.*;

import java.util.HashMap;
import java.util.Map;

public class EquipmentConfig {
    private final Map<Class<? extends Equipment>, String> files;
    private final Map<Class<? extends Equipment>, Integer> equipments;

    public EquipmentConfig(Map<Class<? extends Equipment>, String> files, Map<Class<? extends Equipment>, Integer> equipments) {
        this.files = new HashMap<>(files);
        this.equipments = new HashMap<>(equipments);
    }

    public Map<Class<? extends Equipment>, String> getFiles() {
        return this.files;
    }

    public Map<Class<? extends Equipment>, Integer> getEquipments() {
        return this.equipments;
    }
}
