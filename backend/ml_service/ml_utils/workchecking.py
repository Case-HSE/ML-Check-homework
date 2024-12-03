from .gpt import gpt_prompt
from .ocr import ocr_prompt

from config import role_text


async def __check_homework_from_text_single_pupil(tasks: str, solutions: str) -> str:
    return await gpt_prompt(f"""
    Задания:
        {tasks}
        
    Решения ученика:
        {solutions}
    """, role=role_text)


async def check_homework_from_text_multy_pupil(tasks: str, solutions: list[str]) -> list[str]:
    return [
        await __check_homework_from_text_single_pupil(tasks=tasks, solutions=current_solution)
        for current_solution in solutions
    ]


async def check_homework_from_images_multy_pupil(tasks, solutions: list) -> list[str]:
    return await check_homework_from_text_multy_pupil(
        tasks=await ocr_prompt(tasks),
        solutions=[await ocr_prompt(current_solution) for current_solution in solutions]
    )
