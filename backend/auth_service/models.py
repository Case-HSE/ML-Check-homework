from pydantic import BaseModel


class StatusModel(BaseModel):
    status: str = "success"


class AddAccountModel(BaseModel):
    username: str
    password: str


class OnBoardingModel(BaseModel):
    name: str
    school: str
    class_num: str
    subjects_wishes: list[str]
    favourite_areas: list[str]
    hate_areas: list[str]
    extra_activities: list[str]
    achievements: list[str]
    year_purposes: list[str]
    final_class: int
