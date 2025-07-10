import openai

from loguru import logger

def completion_with_chatgpt(text: str, model: str = "gpt-4") -> str:
 		
    model_id = "ft:gpt-3.5-turbo-1106:personal::BnxP9iwr"  # <- your custom model ID
    logger.info(f"[MODEL] Using model: {model_id}")
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=[
            {"role": "user", "content": text},
        ],
    )
    return response["choices"][0]["message"]["content"]
