import json
import random

input_path = "data/review_summarization.jsonl"
output_path = "data/review_summarization_subset.jsonl"
subset_size = 1500  # Change this number as needed

with open(input_path, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

subset = random.sample(lines, subset_size)

with open(output_path, "w", encoding="utf-8") as outfile:
    for line in subset:
        outfile.write(line)
