import engine.Engine;
import models.config.Config;
import models.config.EquipmentConfig;
import models.equipment.*;
import models.equipment.equipment_collection.Equipments;
import models.player.Player;
import parsers.ConfigParser;
import parsers.EquipmentParser;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.util.*;

public class Resolver {
    public static void main(String[] args) throws IOException {
        if (args.length != 1)
            throw new IllegalArgumentException("Not enough args passed");

        Resolver.initialize(args);
        System.out.println("Finish parsing items");
        Config config = Config.getInstance();
        List<Player> generation = createInitialGeneration(config.getPlayerConfig().getPlayerClass(), config.getPlayerConfig().getCount());
        Player best = Engine.start(generation, config);
        System.out.println(best);
    }

    private static List<Player> createInitialGeneration(Class<? extends Player> type, int count) {
        List<Player> generation = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            generation.add(randomPlayer(type));
        }
        return generation;
    }

    private static Player randomPlayer(Class<? extends Player> type) {
        try {
            return type.getConstructor(double.class, Map.class).newInstance(Player.randomHeight(), randomEquipments());
        } catch (InstantiationException | IllegalAccessException | InvocationTargetException | NoSuchMethodException e) {
            throw new RuntimeException(e);
        }
    }

    private static Map<Class<? extends Equipment>, Equipment> randomEquipments() {
        Map<Class<? extends Equipment>, Equipment> equipmentMap = new HashMap<>();
        equipmentMap.put(Boots.class, Equipments.getInstance().getEquipment(Boots.class));
        equipmentMap.put(Gloves.class, Equipments.getInstance().getEquipment(Gloves.class));
        equipmentMap.put(Helmet.class, Equipments.getInstance().getEquipment(Helmet.class));
        equipmentMap.put(Vest.class, Equipments.getInstance().getEquipment(Vest.class));
        equipmentMap.put(Weapon.class, Equipments.getInstance().getEquipment(Weapon.class));

        return equipmentMap;
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
