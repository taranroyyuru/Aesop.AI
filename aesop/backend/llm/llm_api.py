"""
llm_api - Service for interacting with Large Language Models.
"""

import json
from typing import List, Optional

import litellm
from litellm import completion, embedding
from litellm.types.utils import Choices, ModelResponse
from openai import AzureOpenAI

from aesop.models import LLMMessage

from .llm_model import LLMModel


class LLMApi:
    """Service for interacting with Large Language Models."""

    def __init__(self, model: LLMModel, api_key: Optional[str] = None):
        self.model = model
        self.api_key = api_key
        litellm.set_verbose = True

    def generate_response(
        self, messages: List[LLMMessage], system_prompt: str, **kwargs
    ) -> Optional[str]:
        """Generate a response using the specified model."""

        prepared_messages = [{"role": "system", "content": system_prompt}] + [
            {"role": message.role, "content": message.content} for message in messages
        ]

        completion_kwargs = {
            "api_key": self.api_key,
            "model": self.model.model_name,
            "messages": prepared_messages,
            **kwargs,
        }

        res = completion(**completion_kwargs)
        if isinstance(res, ModelResponse) and isinstance(res.choices[0], Choices):
            return res.choices[0].message.content if res.choices else None

        raise NotImplementedError("Other LiteLLM outputs not implemented yet.")

    def generate_image(self, prompt: str) -> str:
        client = AzureOpenAI(
            api_version="2024-02-01",
            azure_endpoint="https://devan-m2gfjbpu-australiaeast.openai.azure.com",
            api_key="01bf290baa3140eda4340d8b8fb5920e",
        )

        result = client.images.generate(model="dall-e-3", prompt=prompt, n=1)

        image_url = json.loads(result.model_dump_json())["data"][0]["url"]
        return image_url
