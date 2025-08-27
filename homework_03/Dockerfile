FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


WORKDIR /app

# RUN pip install --upgrade pip setuptools whell && \
#     pip install "poetry==1.8.3"

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

# RUN poetry install
RUN poetry install --no-root


COPY /homework_03 .

EXPOSE 8000

CMD ["python", "app.py"]