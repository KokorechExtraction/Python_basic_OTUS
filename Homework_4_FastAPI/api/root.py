from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/root", tags=["root"])
templates = Jinja2Templates("templates")


@router.get(
    "/", response_class=HTMLResponse, summary="Корневой маршрут", description=""
)
def index_view(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Главная"}
    )


@router.get(
    "/about/", response_class=HTMLResponse, summary="Корневой маршрут", description=""
)
def index_view_about(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "title": "О нас"}
    )
