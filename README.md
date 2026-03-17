# Slack LLM Bot

A minimal, production-ready Slack chatbot powered by Large Language
Models (LLMs), built with FastAPI and deployable on Google Cloud Run.

This project is designed as a clean, extensible foundation for building
AI-powered Slack applications.

------------------------------------------------------------------------

## Overview

This repository demonstrates how to:

-   Build a Slack bot using the Events API
-   Process real-time messages with FastAPI
-   Integrate LLMs for intelligent responses
-   Deploy a containerized service to Cloud Run

It intentionally keeps the architecture simple while remaining
production-ready.

------------------------------------------------------------------------

## Architecture

    Slack → FastAPI → LLM → Slack response

Components:

-   Slack Events API for message ingestion
-   FastAPI as the application server
-   LLM provider (OpenAI by default)
-   Cloud Run for scalable deployment

------------------------------------------------------------------------

## Project Structure

    .
    ├── app.py
    ├── Dockerfile
    ├── requirements.txt
    └── src/
        ├── llm.py
        └── slack_handler.py

------------------------------------------------------------------------

## Quickstart

### 1. Clone the repository

    git clone https://github.com/your-username/slack-llm-bot.git
    cd slack-llm-bot

### 2. Create environment file

    SLACK_BOT_TOKEN=your-token
    SLACK_SIGNING_SECRET=your-secret
    OPENAI_API_KEY=your-key

### 3. Run locally

    uvicorn app:api --reload --port 3000

### 4. Expose with ngrok

    ngrok http 3000

### 5. Configure Slack

Set the Request URL:

    https://your-ngrok-url/slack/events

------------------------------------------------------------------------

## Deployment (Cloud Run)

Build and deploy:

    gcloud builds submit --tag gcr.io/YOUR_PROJECT/slack-llm-bot

    gcloud run deploy slack-llm-bot   --image gcr.io/YOUR_PROJECT/slack-llm-bot   --region europe-west1   --platform managed   --allow-unauthenticated   --set-env-vars SLACK_BOT_TOKEN=xxx,SLACK_SIGNING_SECRET=xxx,OPENAI_API_KEY=xxx

Update Slack Request URL:

    https://YOUR-CLOUD-RUN-URL/slack/events

------------------------------------------------------------------------

## Usage

Invite the bot to a channel:

    /invite @Slack LLM Bot

Send a message:

    @Slack LLM Bot hello

------------------------------------------------------------------------

## Design Principles

-   Minimal surface area
-   Clear separation of concerns
-   Production-ready defaults
-   Easy to extend

------------------------------------------------------------------------

## Known Considerations

-   Slack retries events if responses exceed \~3 seconds
-   Duplicate event handling should be implemented for production
-   Cloud Run cold starts may introduce latency on first request

------------------------------------------------------------------------

## Extension Ideas

This project is intentionally simple. It can be extended with:

-   Conversation memory
-   Retrieval-augmented generation (RAG)
-   Multi-tenant architecture
-   Additional platform integrations (Discord, Teams)

------------------------------------------------------------------------

## License

MIT