from fastapi import FastAPI
from routes.api import router
import uvicorn

app=FastAPI()
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        "__main__:app", reload=True, workers = 2
    )



    