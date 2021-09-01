package config.equipmentCollection;

import models.equipment.Equipment;

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

class InMemoryEquipments implements EquipmentCollection {
    private final Map<Class<? extends Equipment>, List<Equipment>> equipmentMap;

    private final Random random;

    InMemoryEquipments(Map<Class<? extends Equipment>, Collection<Equipment>> equipmentMap) {
        this.equipmentMap = new HashMap<>();
        this.random = ThreadLocalRandom.current();

        for (Map.Entry<Class<? extends Equipment>, Collection<Equipment>> entry : equipmentMap.entrySet()) {
            this.equipmentMap.put(entry.getKey(), new ArrayList<>(entry.getValue()));
        }
    }

    @Override
    public Equipment getEquipment(Class<? extends Equipment> equipmentClass) {
        List<Equipment> list = this.equipmentMap.get(equipmentClass);
        return list.get(this.random.nextInt(list.size()));
    }
}
