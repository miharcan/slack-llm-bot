from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

import os
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from fastapi.responses import JSONResponse

from src.slack_handler import handle_message

slack_app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

api = FastAPI()
handler = SlackRequestHandler(slack_app)

@api.post("/slack/events")
async def slack_events(req: Request):
    body = await req.json()

    # 🔥 Handle Slack URL verification
    if body.get("type") == "url_verification":
        return JSONResponse({"challenge": body["challenge"]})

    # otherwise pass to Slack Bolt
    return await handler.handle(req)

@slack_app.event("app_mention")
def mention_listener(event, client, logger):
    if event.get("bot_id"):
        return

    # respond immediately
    client.chat_postMessage(
        channel=event["channel"],
        text="Thinking..."
    )

    # then process
    try:
        handle_message(event, client)
    except Exception as e:
        print("MENTION HANDLER ERROR:", e)
        client.chat_postMessage(
            channel=event["channel"],
            text="I hit an unexpected error. Please try again in a moment.",
        )
