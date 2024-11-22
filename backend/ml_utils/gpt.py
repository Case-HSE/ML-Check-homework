import asyncio

from backend.config import folder_id, role_text, gpt_key
from utils import request

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {gpt_key}"
}

model_uri = f"gpt://{folder_id}/yandexgpt-lite/latest"
default_answer = "К сожалению, я не могу ничего сказать об этом. Давайте сменим тему?"
gpt_url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"


async def gpt_prompt(request_message: str) -> str | None:
    prompt = {
        "modelUri": model_uri,
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "70"
        },
        "messages": [
            {
                "role": "system",
                "text": role_text
            },
            {
                "role": "user",
                "text": request_message
            },
        ]
    }

    request_result = await request(gpt_url, request_headers=headers, json_data=prompt)

    if "error" not in request_result.keys():
        result_text = request_result["result"]["alternatives"][0]["message"]["text"]
        if result_text != default_answer:
            return result_text


if __name__ == '__main__':
    model_result = asyncio.run(gpt_prompt("Привет"))
    print(model_result)