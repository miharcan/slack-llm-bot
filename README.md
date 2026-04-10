> Rename Notice (2026-04-10): this repository was renamed from `slack-llm-bot` to `chat-llm-bot`. Please update scripts and links. Keep old-name redirects/documentation until 2026-05-08.

# Chat LLM Bot

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/framework-fastapi-green)
![Slack](https://img.shields.io/badge/integration-slack-black)
![Cloud Run](https://img.shields.io/badge/deploy-gcp--cloud--run-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Minimal Slack AI chatbot built with FastAPI and LLMs, deployable on
Google Cloud Run with automated CI/CD via GitHub Actions.

------------------------------------------------------------------------

## Overview

This project provides a clean, production-ready foundation for building
Slack chatbots powered by large language models.

It demonstrates:

-   Real-time Slack event handling
-   LLM-based response generation
-   Containerized deployment on Cloud Run
-   Automated deployment using GitHub Actions

------------------------------------------------------------------------

## Architecture

Slack -\> FastAPI -\> LLM -\> Slack response

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

## Quickstart (Local)

### 1. Clone repository

    git clone https://github.com/your-username/slack-llm-bot.git
    cd slack-llm-bot

### 2. Create environment file

    SLACK_BOT_TOKEN=your-token
    SLACK_SIGNING_SECRET=your-secret
    OPENAI_API_KEY=your-key

### 3. Run locally

    uvicorn app:api --reload --port 3000

------------------------------------------------------------------------

## Deployment (Cloud Run)

Build and deploy manually:

    gcloud builds submit --tag gcr.io/YOUR_PROJECT/slack-llm-bot

    gcloud run deploy slack-llm-bot   --image gcr.io/YOUR_PROJECT/slack-llm-bot   --region europe-west1   --platform managed   --allow-unauthenticated   --set-env-vars SLACK_BOT_TOKEN=xxx,SLACK_SIGNING_SECRET=xxx,OPENAI_API_KEY=xxx

------------------------------------------------------------------------

## CI/CD (GitHub Actions)

This project uses GitHub Actions to automatically deploy to Google Cloud Run on push to main, withg the deployment pipeline:

-   Trigger: push to `main`
-   Build Docker image
-   Push to Google Container Registry
-   Deploy to Cloud Run
-   Inject environment variables securely via GitHub Secrets

Required GitHub secrets:

    GCP_PROJECT_ID
    GCP_REGION
    GCP_SA_KEY
    SERVICE_NAME
    SLACK_BOT_TOKEN
    SLACK_SIGNING_SECRET
    OPENAI_API_KEY

------------------------------------------------------------------------

## Usage

Invite the bot to a channel:

    /invite @Slack LLM Bot

Send a message:

    @Slack LLM Bot hello

------------------------------------------------------------------------

## Notes

-   Slack retries events if responses exceed \~3 seconds
-   Duplicate event handling should be implemented for production
-   Cloud Run cold starts may introduce latency

------------------------------------------------------------------------

## License

MIT