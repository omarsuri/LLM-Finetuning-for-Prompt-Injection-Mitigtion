import time
import openai
from harness.base_harness import Harness
from constant.prompt_injection import PromptInjection
from loguru import logger


class ProductReviewHarness(Harness):
    def __init__(self):
        super().__init__()
        self.application_document = "You are an expert product reviewer."

    def run_harness(self, prompt_injection: PromptInjection) -> str:
        try:
            time.sleep(2.5)  # Avoid rate limit

            prompt = prompt_injection.get_attack_prompt()  # ✅ THIS IS THE FIX

            logger.info(f"Injected Prompt: {prompt}")

            response = openai.ChatCompletion.create(
                model="ft:gpt-3.5-turbo-1106:personal::BnxP9iwr",  # Replace if needed
                messages=[
                    {"role": "system", "content": self.application_document},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response["choices"][0]["message"]["content"]

        except Exception as e:
            return f"[ERROR] {str(e)}"
