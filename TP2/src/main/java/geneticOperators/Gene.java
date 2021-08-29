package geneticOperators;

import models.equipment.*;

public enum Gene {
    HEIGHT(double.class),
    BOOTS(Boots.class),
    GLOVES(Gloves.class),
    HELMET(Helmet.class),
    VEST(Vest.class),
    WEAPON(Weapon.class);

    Class<?> clazz;

    Gene(Class<?> clazz) {
        this.clazz = clazz;
    }

    public Class<?> getClazz() {
        return clazz;
    }
}
