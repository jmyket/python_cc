# 8-5: CITIES

def describe_city(city, country = "united states"):
    """Describe a city's location."""
    print(f"{city.title()} is located in the following country: {country.title()}")

describe_city(city = "baltimore")
describe_city(city = "indio")
describe_city(city = "bergen", country = "norway")