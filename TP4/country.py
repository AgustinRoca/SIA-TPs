class Country:
    def __init__(self, name, area, gdp, inflation, life_expectancy, military, population_growth, unemployment):
        self.name = name
        self.area = area
        self.gdp = gdp
        self.inflation = inflation
        self.life_expectancy = life_expectancy
        self.military = military
        self.population_growth = population_growth
        self.unemployment = unemployment

    def as_array(self):
        return [self.area, self.gdp, self.inflation, self.life_expectancy,
                self.military, self.population_growth, self.unemployment]

    def __str__(self):
        return self.name
