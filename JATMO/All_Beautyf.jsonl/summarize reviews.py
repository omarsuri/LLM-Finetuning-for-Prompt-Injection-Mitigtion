import json
import os
import time
from openai import OpenAI # type: ignore

# ✅ Correct usage for OpenAI v1.x
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔁 Paths — adjust if needed
input_path = "data/review_summarization_subset.jsonl"
output_path = "data/review_summarization_labeled.jsonl"

def generate_summary(review_text):
    prompt = f"""You are an expert product reviewer. Summarize the following three customer reviews in one paragraph. Do not reference review numbers or quote text directly. Focus on sentiment, major features, and overall tone.

{review_text}

Summary:"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can switch to gpt-4
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ Error:", e)
        return None

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for i, line in enumerate(infile):
        try:
            item = json.loads(line)
            review_block = item["input"]
            summary = generate_summary(review_block)
            if summary:
                json.dump({"input": review_block, "output": summary}, outfile)
                outfile.write("\n")
                print(f"✅ {i+1}: Summary written.")
            else:
                print(f"⚠️ {i+1}: Skipped (no summary).")
            time.sleep(1.5)  # respect rate limit
        except Exception as err:
            print(f"❌ Line {i+1}: {err}")
