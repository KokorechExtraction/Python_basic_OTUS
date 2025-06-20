"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from typing import List


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.suite.test_reflection import metadata

from homework_04.models import Base, User, Post, engine, Session
from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def create_users(
    session: AsyncSession,
    users_data: List[dict],
) -> None:
    users = [
        User(
            name=user_data["name"],
            username=user_data["username"],
            email=user_data["email"],
        )
        for user_data in users_data
    ]

    session.add_all(users)
    await session.commit()


async def create_posts(
    session: AsyncSession,
    posts_data: List[dict],
) -> None:
    posts = [
        Post(
            title=post_data["title"],
            body=post_data["body"],
        )
        for post_data in posts_data
    ]

    session.add_all(posts)
    await session.commit()


async def async_main():
    async with engine.connect() as session:
        await session.run_sync(Base.metadata.create_all)

    print(Base.metadata.tables)

    async with Session() as session:
        users_data_coro = fetch_users_data()
        posts_data_coro = fetch_posts_data()

        user_data, post_data = await asyncio.gather(
            users_data_coro,
            posts_data_coro,
        )
        await create_users(session, user_data)
        await create_posts(session, post_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
