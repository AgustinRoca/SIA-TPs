package models.equipment.equipment_collection;

import models.equipment.Equipment;

public interface EquipmentCollection {
    Equipment getDifferentEquipment(Equipment equipment);
    Equipment getEquipment(Class<? super Equipment> equipmentClass);
    void reset();
}
