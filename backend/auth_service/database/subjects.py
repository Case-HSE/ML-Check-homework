import json
import os

from auth_service.config import subjects_database_path


subjects_list = [
    "Математика",
    "Русский язык",
    "Литература",
    "История",
    "Физика",
    "Информатика",
    "Английский язык",
    "Обществознание",
    "Химия",
    "Биология",
    "География",
    "ОБЗР",
    "МХК",
    "Экономика",
    "Право",
    "Китайский язык",
    "Физкультура",
    "Испанский язык"
]

if os.path.isfile(subjects_database_path):
    with open(subjects_database_path, "r") as json_file:
        subjects_list = json.load(json_file)
