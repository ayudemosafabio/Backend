from contextlib import asynccontextmanager
from typing import Union
from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis


from app.config.env_config.development import Development
from app.config.env_config.production import Production


def init_lifespan(config:Union[Development, Production]):

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        redis_url = config.REDIS_REATE_LIMIT
        redis_connection = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)
        await FastAPILimiter.init(redis_connection)

        yield

        await redis_connection.close()

    return lifespan