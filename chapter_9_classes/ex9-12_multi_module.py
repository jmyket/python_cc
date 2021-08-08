# EXERCISE 9-12: MULTIPLE MODULES

from chapter_9_classes import user_attr

my_admin = user_attr.Admin()

my_admin.privileges.show_privileges()
my_admin.privileges.privileges = [
    "add", "delete", "ban user", "suspend user", "edit"
]
my_admin.privileges.show_privileges()