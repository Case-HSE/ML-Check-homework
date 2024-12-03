from fastapi import FastAPI
import uvicorn

from auth_service import auth_router
from ml_service import ml_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(ml_router)


@app.get("/")
async def start():
    return "ZOV"


if __name__ == '__main__':
    uvicorn.run(app)
