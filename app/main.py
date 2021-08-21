from __future__ import annotations

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello'}


def test(response):
    return response + 1
