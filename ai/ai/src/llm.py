import os
from openai import OpenAI


class GPT:

    def __init__(self):
        self.client = OpenAI(api_key=os.environ["OPEN_AI_SECRET_KEY"])

    def __call__(
        self,
        sub_model: str,
        prompt: list[dict[str, str]],
    ) -> str:
        completion = self.client.chat.completions.create(
            messages=prompt,
            model=sub_model,
        )
        return completion.choices[0].message.content
