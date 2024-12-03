import os
import json

from auth_service.config import users_onboarding_database_path


onboarding_data = dict()


if os.path.isfile(users_onboarding_database_path):
    with open(users_onboarding_database_path, "r") as json_file:
        onboarding_data = json.load(json_file)
