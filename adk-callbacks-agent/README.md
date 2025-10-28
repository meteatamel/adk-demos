# ADK Callbacks Demo Agent

This is a sample agent that shows different callbacks in ADK:

![Callback Flow](https://google.github.io/adk-docs/assets/callback_flow.png)

## Configure Google AI or Vertex AI

Before running the sample, create a `.env` file with your Google AI or Vertex AI information.

Here's an example for Vertex AI configuration:

```sh
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-google-cloud-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

## Run agent

```sh
adk run .
```

## References

* [Documentation: Callbacks](https://google.github.io/adk-docs/callbacks/)