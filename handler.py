import os
import runpod

from ollama import chat, RequestError, ResponseError


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
    
    try:
        response = chat(
            model=model,
            messages=messages,
            options=args.get("options"),
        )
    except RequestError as error:
        return {"error": f"request error --> {error}"}
    except ResponseError as error:
        return {"error": f"response error --> {error}"}

    return response["message"]["content"]


if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})