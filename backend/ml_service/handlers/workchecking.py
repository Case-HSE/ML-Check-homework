from fastapi import APIRouter, UploadFile
from typing import List

from ml_service.models import MultyTextModel, TextWorkCheckingModel

from ml_service.ml_utils.workchecking import check_homework_from_text_multy_pupil, check_homework_from_images_multy_pupil
from ml_service.ml_utils.utils import bytes_to_base64


router = APIRouter(prefix="/workchecking")


@router.post("/from_text")
async def check_from_text(body: TextWorkCheckingModel) -> MultyTextModel:
    tasks = "\n".join(body.tasks)
    model_answer = await check_homework_from_text_multy_pupil(
        tasks=tasks,
        solutions=body.texts
    )
    return MultyTextModel(texts=model_answer)


@router.post("/from_images")
async def check_from_images(
        tasks: List[UploadFile],
        solutions: List[UploadFile]
) -> MultyTextModel:
    tasks = [bytes_to_base64(await current_file.read()) for current_file in tasks]
    solutions = [bytes_to_base64(await current_file.read()) for current_file in solutions]
    model_answer = await check_homework_from_images_multy_pupil(
        tasks=tasks,
        solutions=solutions
    )
    return MultyTextModel(texts=model_answer)
