package parsers;

import models.equipment.Equipment;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;

public abstract class EquipmentParser {
    private static final String ID_HEADER = "id";
    private static final String FORCE_HEADER = "fu";
    private static final String AGILITY_HEADER = "ag";
    private static final String INTELLIGENCE_HEADER = "ex";
    private static final String ENDURANCE_HEADER = "re";
    private static final String HEALTH_HEADER = "vi";

    public static Collection<Equipment> parse(Class<? extends Equipment> equipmentClass, BufferedReader reader) throws IOException {
        Map<String, Integer> headerMap = EquipmentParser.headerMap(reader);
        String line;
        LinkedList<Equipment> list = new LinkedList<>();

        while ((line = reader.readLine()) != null) {
            list.add(EquipmentParser.parseLine(equipmentClass, headerMap, line.split("\t")));
        }

        return list;
    }

    private static Map<String, Integer> headerMap(BufferedReader reader) throws IOException {
        Map<String, Integer> headerMap = new HashMap<>();
        String[] header = reader.readLine().split("\t");
        for (int i = 0; i < header.length; i++) {
            header[i] = header[i].toLowerCase();
            headerMap.put(header[i], i);

            switch (header[i]) {
                case ID_HEADER:
                    break;
                case FORCE_HEADER:
                case AGILITY_HEADER:
                case INTELLIGENCE_HEADER:
                case ENDURANCE_HEADER:
                case HEALTH_HEADER:
                    headerMap.put(header[i], i);
                    break;
                default: throw new IllegalArgumentException();
            }
        }

        return headerMap;
    }

    private static Equipment parseLine(Class<? extends Equipment> equipmentClass, Map<String, Integer> headerMap, String[] lineItems) {
        try {
            return equipmentClass
                    .getConstructor(int.class, double.class, double.class, double.class, double.class, double.class)
                    .newInstance(
                            Integer.parseInt(lineItems[headerMap.get(ID_HEADER)]),
                            Double.parseDouble(lineItems[headerMap.get(FORCE_HEADER)]),
                            Double.parseDouble(lineItems[headerMap.get(AGILITY_HEADER)]),
                            Double.parseDouble(lineItems[headerMap.get(ENDURANCE_HEADER)]),
                            Double.parseDouble(lineItems[headerMap.get(INTELLIGENCE_HEADER)]),
                            Double.parseDouble(lineItems[headerMap.get(HEALTH_HEADER)])
                    );
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }
}
