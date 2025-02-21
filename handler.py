import runpod

from ollama import chat


def handler(event: dict[str, dict]):
    prompt = event["input"].get("prompt")
    if prompt is None:
        return {"error": "no prompt given in input."}
    
    model = event["input"].get("model") or "llama3"
    
    response = chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.message.content


if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})