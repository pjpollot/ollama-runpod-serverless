import os
import runpod

from ollama import chat


def handler(event: dict[str, dict]):
    args = event["input"]

    prompt = args.get("prompt")

    if prompt is None:
        messages = args.get("messages")
        if messages is None:
            return {"error": "no prompt or messages given in input."}
        
    else:
        system = args.get("system")

        messages = []
        if system is not None:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
    
    model = args.get("model") or os.getenv("MODEL_NAME")
    
    response = chat(
        model=model,
        messages=messages,
    )

    return response.message.content


if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})