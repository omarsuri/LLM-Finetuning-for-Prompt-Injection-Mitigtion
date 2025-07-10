import os
import json
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Replace with your fine-tuned model ID
fine_tuned_model_id = "ft:gpt-3.5-turbo-1106:personal::BnxP9iwr"

# Load red-teamed prompts
with open("summarization_attacks.json", "r", encoding="utf-8") as f:
    attack_prompts = json.load(f)

# Evaluate each prompt
for i, item in enumerate(attack_prompts[:20]):  # limit to 20 for demo
    user_input = item["input"]
    messages = [
        {"role": "system", "content": "You are an expert product reviewer."},
        {"role": "user", "content": user_input}
    ]

    # Fine-tuned model response
    try:
        jatmo_resp = client.chat.completions.create(
            model=fine_tuned_model_id,
            messages=messages,
            temperature=0.0
        ).choices[0].message.content.strip()
    except Exception as e:
        jatmo_resp = f"[Error: {e}]"

    # GPT-3.5 baseline response
    try:
        base_resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.0
        ).choices[0].message.content.strip()
    except Exception as e:
        base_resp = f"[Error: {e}]"

    # Print side-by-side results
    print(f"\n🧪 Prompt #{i+1}")
    print(f"💬 Input: {user_input}")
    print(f"🔒 JATMO: {jatmo_resp}")
    print(f"📦 GPT-3.5: {base_resp}")
    print("-" * 80)
