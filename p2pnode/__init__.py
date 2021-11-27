import aioredis
import requests

from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter

import p2pnode.v1 as v1

app = FastAPI(title="MetaExchange Node", debug=True)

HOST = "127.0.0.1:8000"
NODE_HOST = "127.0.0.1:8001"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    requests.post(f'http://{HOST}/api/v1/blockchain/nodes/register', json={"nodes":[NODE_HOST]})
    redis = await aioredis.create_redis_pool("redis://localhost")
    await FastAPILimiter.init(redis)

app.include_router(v1.v1, prefix="/node")

@app.get("/")
async def index_page():
    return {
        ""
    }