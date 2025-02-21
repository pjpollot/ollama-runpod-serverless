# ollama for runpod serverless

A basic template to run a LLM with RunPod serverless.

## Build

```sh
docker build -t <image name> . [--build-arg MODEL_NAME=<model name>]
```

## Example of inputs

### Prompt only

```json
{
    "input": {
        "prompt": "Hello, world!" 
    }
}
```

We can also pass a system prompt as an input:

```json
{
    "input": {
        "system": "You are GlaDOS.",
        "prompt": "Hello, world!"
    }
}
```

### Messages

```json
{
    "input": {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": "You are GlaDOS."},
            {"role": "user", "content": "Hello, world!"}
        ]
    }
}
```
