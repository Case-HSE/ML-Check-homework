import asyncio

from config import ocr_key

from .utils import request, encode_image


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {ocr_key}"
}

ocr_url = "https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText"


async def ocr_prompt(image_content) -> str:
    if isinstance(image_content, list):
        request_result = []
        for current_image_content in image_content:
            request_result.append(await ocr_prompt(image_content=current_image_content))
        return "\n".join(request_result)

    else:
        data = {
            "mimeType": "JPEG",
            "languageCodes": ["ru", "en"],
            "model": "handwritten",
            "content": image_content
        }

        request_result = await request(url=ocr_url, json_data=data, request_headers=headers)
        if "result" in request_result:
            return request_result["result"]["textAnnotation"]["fullText"]
        return "Error!"



if __name__ == '__main__':
    processed_image = encode_image("test.jpg")
    result = asyncio.run(ocr_prompt(processed_image))
    print(result)
