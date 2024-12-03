import os
import json

from auth_service.config import credentials_database_path


credentials_data = dict()


if os.path.isfile(credentials_database_path):
    with open(credentials_database_path, "r") as json_file:
        credentials_data = json.load(json_file)
