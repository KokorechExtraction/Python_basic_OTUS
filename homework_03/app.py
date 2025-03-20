from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Приложение для проверки контейнера",
    description="Приложение возвращает JSON объект",
    version="1.0.0",
)


@app.get(
    "/ping/",
    status_code=200,
    summary="Возвращение JSON объект",
    description="Возвращает JSON объект",
)
def view():
    return {"message": "pong"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
