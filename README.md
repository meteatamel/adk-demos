# Agent Development Kit (ADK) Tutorial

Create and activate a Python environment:

```shell
python -m venv .venv
source .venv/bin/activate
```

Install ADK:

```shell
pip install google-adk
```

Copy `dotenv` file to `.env` file and fill your Google AI or Vertex AI information. Here's an
example for Vertex AI configuration:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=genai-atamel
GOOGLE_CLOUD_LOCATION=us-central1
```

Deploy to Cloud Run:

```shell
adk deploy cloud_run \
  --project="google-cloud-project-id" \
  --region="us-central1" \
  --service_name="travel-helper-service" \
  --with_ui \
  ./travel_helper
```