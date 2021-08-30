# 8-6: CITY NAMES

def city_country(city, country):
    """Return formatted City, Country."""
    formal_nm = f"{city.title()}, {country.title()}"
    return formal_nm

city_country("philadelphia", "united states")
city_country("london", "england")
city_country("toronto", "canada")