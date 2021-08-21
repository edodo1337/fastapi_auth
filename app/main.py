from __future__ import annotations

import fastapi
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root() -> fastapi.Response:
    return {'message': 'Hello'}


def test(response: int) -> int:
    return response + 1
