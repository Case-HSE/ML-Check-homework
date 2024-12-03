from fastapi import APIRouter, UploadFile

from ml_utils.gpt import gpt_prompt
from ml_utils.ocr import ocr_prompt
from ml_utils.utils import bytes_to_base64

from models import TextModel, TextResponseModel


router = APIRouter(prefix="/ai")


@router.post("/gpt/prompt")
async def gpt_prompt_event(body: TextModel) -> TextResponseModel:
    model_answer = await gpt_prompt(request_message=body.text)
    return TextResponseModel(text=model_answer)


@router.post("/ocr/prompt")
async def ocr_prompt_event(image: UploadFile) -> TextResponseModel:
    image_content = bytes_to_base64(await image.read())
    model_answer = await ocr_prompt(image_content=image_content)
    return TextResponseModel(text=model_answer)
