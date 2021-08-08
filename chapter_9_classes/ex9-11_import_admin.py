# EXERCISE 9-11: IMPORTED ADMIN

from chapter_9_classes import users_all as adn

my_admin = adn.Admin()

my_admin.privileges.show_privileges()
my_admin.privileges.privileges = [
    "add", "delete", "ban user", "suspend user", "edit"
]
my_admin.privileges.show_privileges()