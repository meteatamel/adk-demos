# Setup 

Before you run any samples, make sure you follow these steps. 

Set your project id in `gcloud`:

```shell
gcloud config set core/project your-google-cloud-project-id
```

Authenticate:

```shell
gcloud auth application-default login
```

Create and activate a Python virtual environment:

```shell
python -m venv .venv
source .venv/bin/activate
```

Install ADK:

```shell
pip install google-adk
```

Copy `dotenv` file to `.env` file and fill your Google AI or Vertex AI information.

Here's an example for Vertex AI configuration:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=genai-atamel
GOOGLE_CLOUD_LOCATION=us-central1
```