"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp
import logging
from typing import List

log = logging.getLogger(__name__)

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> List[dict]:
    log.info("Fetching %s", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
    log.info("got result from %s: %s", url, result)
    return result


async def fetch_users_data():
    data = await fetch_json(USERS_DATA_URL)
    log.info("Fetched data: %s", data)
    return data


async def fetch_posts_data():
    data = await fetch_json(POSTS_DATA_URL)
    log.info("Fetched data: %s", data)
    return data
