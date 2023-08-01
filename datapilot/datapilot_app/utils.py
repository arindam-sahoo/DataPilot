import os
from django.contrib.auth.models import User
from django.conf import settings

def assign_database(user):
    # Replace this function with logic to assign the database to the user
    # For demonstration purposes, we will use a simple approach
    database_name = f"{user.username}.db"
    database_path = os.path.join(settings.BASE_DIR, "user_databases", database_name)

    # Check if the database file already exists for the user
    if os.path.exists(database_path):
        return database_name

    # Create the database file for the user
    with open(database_path, 'w'):
        pass

    return database_name
