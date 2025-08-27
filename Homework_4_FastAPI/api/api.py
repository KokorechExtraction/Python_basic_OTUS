from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import ValidationError

from Homework_4_FastAPI.models.bear import bears, Bear
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/api", tags=["api"])
templates = Jinja2Templates("templates")


@router.get(
    "/goal/",
    response_class=HTMLResponse,
    summary="ГООООООЛ",
    description="ГООООООЛ",
)
def get_goal(request: Request):

    return templates.TemplateResponse("goal.html", {"request": request})


@router.get(
    "/bears",
    response_class=HTMLResponse,
    summary="Получение всех медведей",
    description="Получение записей всех медведей",
)
def get_all_bears(request: Request):

    return templates.TemplateResponse(
        "bear_some.html", {"request": request, "bears": bears}
    )


@router.get(
    "/bears/{bear_id}",
    response_class=HTMLResponse,
    summary="Получение медведей по id",
    description="Получение записей всех медведей",
)
def get_bear_by_id(request: Request, bear_id: int):

    bear = next((bear for bear in bears if bear["id"] == bear_id), None)
    if not bear:
        return templates.TemplateResponse(
            "goal.html", {"request": request, "title": "Не найдено"}
        )
    return templates.TemplateResponse(
        "bear_some.html", {"request": request, "bear": bear}
    )


@router.post(
    "/bears/add_bear",
    response_class=HTMLResponse,
    summary="Добавление медведя",
)
def create_bear(request: Request, name=Form(...), age=Form(...)):

    new_id = max(int(bear.id) for bear in bears) + 1
    # bears.append({"id": new_id, "name": name, "age": age})

    try:
        bears.append(Bear(id=new_id, name=name, age=age))

    except ValidationError as e:
        templates.TemplateResponse("bear_some.html", {"request": request})

    templates.TemplateResponse("bear_some.html", {"request": request})
