from fastapi import APIRouter

from auth_service.models import SubjectModel, StatusModel

from auth_service.database.subjects import subjects_list


router = APIRouter(prefix="/subjects")


@router.get("/getsublist")
async def get_subject_list() -> list[str]:
    return subjects_list


@router.post("/addsubject")
async def add_subject(body: SubjectModel) -> StatusModel:
    subjects_list.append(body.subject)
    return StatusModel()


@router.delete("/deletesubject")
async def delete_subject(body: SubjectModel) -> StatusModel:
    subjects_list.remove(body.subject)
    return StatusModel()
