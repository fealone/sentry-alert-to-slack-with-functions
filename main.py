import json
import os
from typing import Any, Dict

from agraffe import Agraffe

from fastapi import FastAPI, Request

import requests

app = FastAPI()


@app.post("/sentry")
async def printf(request: Request) -> Dict[str, str]:
    body = await request.json()
    payload = {"text": (f"An error occurred, for details from the issue below url."
                        f"\r\n{body['url']}")}
    res = requests.post(os.environ["SLACK_ENDPOINT"],
                        data=json.dumps(payload),
                        headers={"Content-Type": "application/json"})
    if res.status_code != 200:
        raise Exception(f"Error request to slack. [{res.status_code}]")
    return {}


def entry_point(request: Any) -> Agraffe:
    agraffe = Agraffe(app)
    return agraffe(request)
