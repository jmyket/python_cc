# 8-13: USER PROFILE

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

my_profile = build_profile(
    first = "josh", last = "myket", age = 35, location = 'U.S.', height = 71
)

print(my_profile)