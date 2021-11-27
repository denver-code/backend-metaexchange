import aioredis

from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter

import node.v1 as v1

app = FastAPI(title="MetaExchange Node", debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    redis = await aioredis.create_redis_pool("redis://localhost")
    await FastAPILimiter.init(redis)

app.include_router(v1.api, prefix="/node")