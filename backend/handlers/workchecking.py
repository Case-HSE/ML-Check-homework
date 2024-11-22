from fastapi import APIRouter, UploadFile
from typing import List

from models import MultyTextModel, TextWorkCheckingModel

from ml_utils.workchecking import check_homework_from_text_multy_pupil, check_homework_from_images_multy_pupil
from ml_utils.utils import bytes_to_base64


router = APIRouter()


@router.post("/workchecking/from_text")
async def check_from_text(body: TextWorkCheckingModel) -> MultyTextModel:
    model_answer = await check_homework_from_text_multy_pupil(
        tasks=body.tasks,
        solutions=body.texts
    )
    return MultyTextModel(texts=model_answer)


@router.post("/workchecking/from_images")
async def check_from_images(tasks: str, solutions: List[UploadFile]) -> MultyTextModel:
    solutions = [bytes_to_base64(await current_file.read()) for current_file in solutions]
    model_answer = await check_homework_from_images_multy_pupil(
        tasks=tasks,
        solutions=solutions
    )
    return MultyTextModel(texts=model_answer)
