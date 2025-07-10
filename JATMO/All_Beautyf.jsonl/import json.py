import json
import os

input_path = "All_Beauty.jsonl"
output_path = "data/review_summarization.jsonl"

# Make sure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

inputs = []
review_group = []

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for line in infile:
        try:
            review = json.loads(line)
            text = review.get("text", "").strip()
            if not text:
                continue
            review_group.append(text)

            if len(review_group) == 3:
                review_text = ""
                for idx, r in enumerate(review_group):
                    review_text += f"Review #{idx+1}: {r} "

                # You can later use GPT to summarize automatically
                summary = "Summary: [write your summary here]"

                data = {"input": review_text.strip(), "output": summary}
                outfile.write(json.dumps(data) + "\n")
                review_group = []

        except Exception as e:
            print(f"Skipping a line due to error: {e}")
