from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Homework_4_FastAPI.api.api import router as bear_router
import uvicorn


templates = Jinja2Templates("templates")


app = FastAPI(
    title="Приложение для работы с записями",
    description="Приложение для добавления, просмотра и управления записями",
    version="1.0.0",
)


app.include_router(bear_router)


@app.get("/", response_class=HTMLResponse, summary="Корневой маршрут", description="")
def index_view(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Главная"}
    )


@app.get(
    "/about/", response_class=HTMLResponse, summary="Корневой маршрут", description=""
)
def index_view_about(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "title": "О нас"}
    )


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)
