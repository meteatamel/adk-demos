# Setup 

Before you run any samples, make sure you follow these steps, either from Cloud Shell or your 
local `gcloud` installation. 

## Set gcloud

Check if your project is set:

```shell
gcloud config list

...
[core]
project = your-google-cloud-project-id
```

If not, set your project id:

```shell
gcloud config set core/project your-google-cloud-project-id
```

If not in Cloud Shell (i.e. running locally), authenticate:

```shell
gcloud auth application-default login
```

Enable Vertex AI API:

```shell
gcloud services enable aiplatform.googleapis.com
```

## Get the code

Clone the repository:

```shell
git clone https://github.com/meteatamel/adk-demos.git
```

## Set Python environment

Navigate to the repository. Create and activate a Python virtual environment:

```shell
cd adk-demos
python -m venv .venv
source .venv/bin/activate
```

Install ADK:

```shell
pip install -r requirements.txt
```

## Configure Google AI or Vertex AI 

Copy `dotenv` file to `.env` file and fill your Google AI or Vertex AI information.

Here's an example for Vertex AI configuration:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-google-cloud-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```