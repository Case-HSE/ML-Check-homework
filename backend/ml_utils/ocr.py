import asyncio

from backend.config import ocr_key

from utils import request, encode_image


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {ocr_key}"
}

ocr_url = "https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText"


async def ocr_prompt(image_content) -> str | list[str]:
    if isinstance(image_content, list):
        request_result = []
        for current_image_content in image_content:
            request_result.append(await ocr_prompt(image_content=current_image_content))
        return request_result

    else:
        data = {
            "mimeType": "JPEG",
            "languageCodes": ["ru", "en"],
            "model": "handwritten",
            "content": image_content
        }

        request_result = await request(url=ocr_url, json_data=data, request_headers=headers)
        return request_result["result"]["textAnnotation"]["fullText"]



if __name__ == '__main__':
    processed_image = encode_image("test.jpg")
    result = asyncio.run(ocr_prompt(processed_image))
    print(result)
