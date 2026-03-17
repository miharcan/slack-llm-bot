from src.llm import generate_reply

processed_events = set()

def handle_message(event, client):
    event_id = event.get("ts")

    if event_id in processed_events:
        return

    processed_events.add(event_id)

    text = event.get("text")
    channel = event.get("channel")

    if not text:
        return

    reply = generate_reply(text)

    client.chat_postMessage(
        channel=channel,
        text=reply
    )