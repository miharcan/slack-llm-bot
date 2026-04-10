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

    # Slack app mentions include a bot token like <@U123...>; remove it for cleaner prompts.
    cleaned_text = " ".join(
        token for token in text.split() if not (token.startswith("<@") and token.endswith(">"))
    ).strip()
    if not cleaned_text:
        cleaned_text = text

    try:
        reply = generate_reply(cleaned_text)
    except Exception as e:
        print("LLM ERROR:", e)
        client.chat_postMessage(
            channel=channel,
            text="I hit an error while generating a reply. Please try again in a moment.",
        )
        return

    if not reply:
        reply = "I do not have a response right now. Please try again."

    client.chat_postMessage(
        channel=channel,
        text=reply
    )
