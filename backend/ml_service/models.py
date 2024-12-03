from pydantic import BaseModel


class TextModel(BaseModel):
    text: str


class TextResponseModel(TextModel):
    status: str = "success"


class MultyTextModel(BaseModel):
    texts: list[str]


class TextWorkCheckingModel(MultyTextModel):
    tasks: str
