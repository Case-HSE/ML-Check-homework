import base64
import aiohttp


async def request(url: str, json_data: dict, request_headers: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data, headers=request_headers) as resp:
            return await resp.json()


def encode_image(file_path: str):
    with open(file_path, "rb") as fid:
        file_content = fid.read()
    return base64.b64encode(file_content).decode("utf-8")
