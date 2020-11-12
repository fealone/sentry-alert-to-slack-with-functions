import json
import os
from typing import Dict

from agraffe import Agraffe, Service

from fastapi import FastAPI, Request

import requests

app = FastAPI()


@app.post("/sentry")
async def sentry(request: Request) -> Dict[str, str]:
    body = await request.json()
    payload = {"text": (f"An error occurred, for details from the issue below url."
                        f"\r\n{body['url']}")}
    res = requests.post(os.environ["SLACK_ENDPOINT"],
                        data=json.dumps(payload),
                        headers={"Content-Type": "application/json"})
    if res.status_code != 200:
        raise Exception(f"Error request to slack. [{res.status_code}]")
    return {}


platform = os.environ.get("PLATFORM", "GCP")

if platform == "GCP":
    entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)
elif platform == "AWS":
    entry_point = Agraffe.entry_point(app, Service.aws_lambda)
else:
    Exception(f"Unsupported platform of {platform}")
