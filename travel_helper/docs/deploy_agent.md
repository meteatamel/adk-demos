# Travel Helper Agent - Deploy Agent

ADK has a few [deployment options](https://google.github.io/adk-docs/deploy/): Vertex AI Agent Engine, Cloud Run, or 
self-managed.  

# Deploy to Cloud Run

Let's deploy the agent to Cloud Run with the dev UI enabled. 

First make sure the necessary APIs are enabled:

```shell
gcloud services enable artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  run.googleapis.com
```

Then, deploy using the `adk` tool:

```shell
adk deploy cloud_run \
  --project="your-project-id" \
  --region="us-central1" \
  --service_name="travel-helper-service" \
  --with_ui \
  ./travel_helper
```

This builds a container for the agent and deploys to Cloud Run. You can visit the default URL of the Cloud Run service
to interact with the agent.

# Deploy to Vertex AI Agent Engine

> [!CAUTION]
> There's currently a bug in `adk deploy agent_engine` with relative imports that prevents travel_helper
> being deployed to Agent Engine. Once that's solved, instructions here should just work.

Let's deploy the agent to Vertex AI Agent.

First, make sure the agent engine libraries are installed:

```shell
pip install 'google-cloud-aiplatform[agent_engines]'
```

Create a staging bucket for the agent engine:

```shell
PROJECT_ID=your-project-id
STAGING_BUCKET=gs://$PROJECT_ID-agent-engine-staging
gsutil mb $STAGING_BUCKET
```

Deploy using the `adk` tool:

```shell
adk deploy agent_engine \
  --project $PROJECT_ID \
  --region us-central1 \
  --display_name travel-helper-agent \
  --staging_bucket $STAGING_BUCKET \
  --trace_to_cloud \
  ./travel_helper
```

---

Go back to [travel_helper](../README.md) to continue.
