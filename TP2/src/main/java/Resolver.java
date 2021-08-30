import models.config.Config;
import models.config.EquipmentConfig;
import models.equipment.*;
import models.equipment.equipment_collection.Equipments;
import parsers.ConfigParser;
import parsers.EquipmentParser;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

import java.io.*;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class Resolver {
    public static void main(String[] args) throws IOException {
        if (args.length != 1)
            throw new IllegalArgumentException("Not enough args passed");

        Resolver.initialize(args);

        // TODO: Aplicar todos los algo
    }

    private static void initialize(String[] args) throws IOException {
        ConfigParser.parse(new FileInputStream(args[0]));

        if (Config.getInstance().getEquipmentConfig().isInMemory()) {
            Map<Class<? extends Equipment>, Collection<Equipment>> equipmentMap = new HashMap<>();

            Resolver.parseEquipment(Boots.class, equipmentMap);
            Resolver.parseEquipment(Gloves.class, equipmentMap);
            Resolver.parseEquipment(Helmet.class, equipmentMap);
            Resolver.parseEquipment(Vest.class, equipmentMap);
            Resolver.parseEquipment(Weapon.class, equipmentMap);

            Equipments.createInMemoryInstance(equipmentMap);
        } else {
            // TODO: Create File Instance

            throw new NotImplementedException();
        }
    }

    private static void parseEquipment(Class<? extends Equipment> equipmentClass, Map<Class<? extends Equipment>, Collection<Equipment>> equipmentMap) throws IOException {
        equipmentMap.put(
                equipmentClass,
                EquipmentParser.parse(
                        equipmentClass,
                        new BufferedReader(new FileReader(Config.getInstance().getEquipmentConfig().getBoots()))
                )
        );
    }
}
