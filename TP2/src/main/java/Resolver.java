import config.containers.EquipmentConfig;
import engine.Engine;
import config.containers.Config;
import models.equipment.*;
import config.equipmentCollection.Equipments;
import models.player.Player;
import config.parsers.ConfigParser;
import config.parsers.EquipmentParser;
import serializer.CSVGenerationSerializer;

import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.util.*;

public class Resolver {
    public static void main(String[] args) throws IOException {
        if (args.length != 1)
            throw new IllegalArgumentException("Not enough args passed");

        System.out.println("Initializing engine");

        ConfigParser.parse(new FileInputStream(args[0]));
        Config config = Config.getInstance();
        CSVGenerationSerializer generationSerializer = new CSVGenerationSerializer(config.getOutputPath());
        Resolver.initialize();

        System.out.println("Finish initialization");

        List<Player> generation = createInitialGeneration(config.getPlayerConfig().getPlayerClass(), config.getPlayerConfig().getCount());

        Engine engine = new Engine(generationSerializer);

        Player best = engine.run(generation);
        generationSerializer.close();

        System.out.println(best);
    }

    private static List<Player> createInitialGeneration(Class<? extends Player> type, int count) {
        List<Player> generation = new ArrayList<>(count);
        for (int i = 0; i < count; i++) {
            generation.add(randomPlayer(type));
        }
        return generation;
    }

    private static Player randomPlayer(Class<? extends Player> type) {
        try {
            if (Config.getInstance().getPlayerConfig().getHeightConfig().getPrecalculated())
                return type.getConstructor(Map.class).newInstance(randomEquipments());

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

    private static void initialize() throws IOException {
        EquipmentConfig equipmentConfig = Config.getInstance().getEquipmentConfig();

        Map<Class<? extends Equipment>, Collection<Equipment>> equipmentMap = new HashMap<>();

        for (Map.Entry<Class<? extends Equipment>, String> entry : equipmentConfig.getFiles().entrySet()) {
            Resolver.parseEquipment(entry.getKey(), equipmentMap, entry.getValue(), equipmentConfig.getEquipments().get(entry.getKey()));
        }

        Equipments.createInMemoryInstance(equipmentMap);
    }

    private static void parseEquipment(
            Class<? extends Equipment> equipmentClass,
            Map<Class<? extends Equipment>, Collection<Equipment>> equipmentMap,
            String filename,
            Integer chosenId
    ) throws IOException
    {
        equipmentMap.put(
                equipmentClass,
                EquipmentParser.parse(
                        equipmentClass,
                        new BufferedReader(new FileReader(filename)),
                        chosenId
                )
        );
    }
}
