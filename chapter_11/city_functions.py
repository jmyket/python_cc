def city_location(city, country, population = None):
    """Formatted city location string."""
    if population:
        full_str = f"{city.title()}, {country.title()} - population {population}"
    else:
        full_str = f"{city.title()}, {country.title()}"
    return full_str