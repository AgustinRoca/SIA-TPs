package config.equipmentCollection;

import models.equipment.Equipment;

import java.util.Collection;
import java.util.Map;

public abstract class Equipments {
    private static EquipmentCollection instance;

    public static EquipmentCollection getInstance() {
        return instance;
    }

    public static EquipmentCollection createInMemoryInstance(Map<Class<? extends Equipment>, Collection<Equipment>> equipmentMap) {
        if (instance != null)
            return instance;

        instance = new InMemoryEquipments(equipmentMap);
        return instance;
    }
}
