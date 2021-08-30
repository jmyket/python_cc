# 8-14: CARS

def make_car(make, model, **kwargs):
    """Build a dictionary containing information on a car."""
    kwargs['make'] = make.title()
    kwargs['model'] = model.title()
    return kwargs

my_car = make_car(
    make = "suburu", model = "forester", year = 2020, color = "white", transmission = "automatic"
)

print(my_car)