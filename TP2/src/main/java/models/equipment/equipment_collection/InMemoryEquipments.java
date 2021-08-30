package models.equipment.equipment_collection;

import models.equipment.Equipment;

import java.util.*;

class InMemoryEquipments implements EquipmentCollection {
    private final Map<Class<? extends Equipment>, LinkedList<Equipment>> originalEquipmentMap;
    private final Map<Class<? extends Equipment>, LinkedList<Equipment>> equipmentMap;

    private final Random random;

    InMemoryEquipments(Map<Class<? extends Equipment>, Collection<Equipment>> equipmentMap) {
        this.originalEquipmentMap = new HashMap<>();
        this.equipmentMap = new HashMap<>();
        this.random = new Random();

        for (Map.Entry<Class<? extends Equipment>, Collection<Equipment>> entry : equipmentMap.entrySet()) {
            this.originalEquipmentMap.put(entry.getKey(), new LinkedList<>(entry.getValue()));
            this.equipmentMap.put(entry.getKey(), new LinkedList<>(entry.getValue()));
        }
    }

    @Override
    public Equipment getDifferentEquipment(Equipment equipment) {
        Equipment e = equipment;
        int i = 0;
        LinkedList<Equipment> list = null;

        while (e == equipment) {
            list = this.equipmentMap.get(equipment.getClass());
            i = this.random.nextInt(list.size());
            e = list.get(i);
        }
        list.remove(i);

        return e;
    }

    @Override
    public Equipment getEquipment(Class<? super Equipment> equipmentClass) {
        LinkedList<Equipment> list = this.equipmentMap.get(equipmentClass);
        return list.remove(this.random.nextInt(list.size()));
    }

    @Override
    public void reset() {
        this.equipmentMap.clear();

        for (Map.Entry<Class<? extends Equipment>, LinkedList<Equipment>> entry : this.originalEquipmentMap.entrySet()) {
            this.equipmentMap.put(entry.getKey(), new LinkedList<>(entry.getValue()));
        }
    }
}
