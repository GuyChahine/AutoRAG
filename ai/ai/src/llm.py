import os
from openai import OpenAI

from ai.models import llm as models


class GPT:

    def __init__(self):
        self.client = OpenAI(api_key=os.environ["OPEN_AI_SECRET_KEY"])

    def __call__(
        self,
        sub_model: str,
        prompt: list[dict[str, str]],
    ) -> models.LLMResponse:
        completion = self.client.chat.completions.create(
            messages=prompt,
            model=sub_model,
        )
        return models.LLMResponse(
            output=completion.choices[0].message.content,
            prompt_tokens=completion.usage.prompt_tokens,
            completion_tokens=completion.usage.completion_tokens,
        )
