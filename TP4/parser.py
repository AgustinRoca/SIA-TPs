from country import Country


class Parser:
    delimiter = ','

    def parse(self, filename):
        file = open(filename)
        titles = file.readline().replace('"', '').strip().split(self.delimiter)
        titles.pop(0)  # remove the names
        countries = []
        for line in file.readlines():
            fields = line.split(self.delimiter)

            name = fields[0].replace('"', '')
            area = int(fields[1])
            gdp = int(fields[2])
            inflation = float(fields[3])
            life_expectancy = float(fields[4])
            military = float(fields[5])
            population_growth = float(fields[6])
            unemployment = float(fields[7])

            country = Country(name, area, gdp, inflation, life_expectancy, military, population_growth, unemployment)
            countries.append(country)
        return titles, countries


