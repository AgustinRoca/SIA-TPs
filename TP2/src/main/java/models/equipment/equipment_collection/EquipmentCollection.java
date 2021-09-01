package models.equipment.equipment_collection;

import models.equipment.Equipment;

public interface EquipmentCollection {
    Equipment getEquipment(Class<? extends Equipment> equipmentClass);
}
