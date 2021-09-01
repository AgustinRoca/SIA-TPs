package config.equipmentCollection;

import models.equipment.Equipment;

public interface EquipmentCollection {
    Equipment getEquipment(Class<? extends Equipment> equipmentClass);
}
