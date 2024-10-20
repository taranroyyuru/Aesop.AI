import json
from typing import List

import requests
from litellm import AzureOpenAI
from pydantic import BaseModel, Field

from aesop.backend.llm import LLMApi, LLMModel
from aesop.backend.llm.prompts import STORY_GENERATION
from aesop.models import LLMMessage
from config import config


class StoryContent(BaseModel):
    story: str = Field(..., description="First part of the story narrative.")
    image_description: str = Field(
        ...,
        description="Vivid description of the image that represents this part of the story.",
    )


class StoryResponse(BaseModel):
    title: str = Field(..., description="The title of the story.")
    summary: str = Field(..., description="Short story description.")
    general_description: str = Field(..., description="The generated story.")
    subject: str = Field(
        ...,
        description="Subject area this story pertains to (e.g., 'math', 'science', 'history').",
    )
    content: List[StoryContent] = Field(
        ...,
        description="List of story parts, each with narrative and image description.",
    )


def parse_llm_response(response_json: dict) -> StoryResponse:
    return StoryResponse(**response_json)


def generate_story(
    character_description: str, story_description: str, reading_level: str
) -> StoryResponse:
    llm_api = LLMApi(
        model=LLMModel.GROQ_LLAMA_70B, api_key=config.llm_config.qrok_api_key
    )

    llm_response = llm_api.generate_response(
        system_prompt=STORY_GENERATION,
        messages=[
            LLMMessage(
                role="user",
                content=(
                    "I want my story's main character to be:"
                    + f"{character_description}\n\n"
                    "I want my story to be about:" + f"{story_description}\n\n"
                    "I want my story to be in the following reading level:"
                    + f"{reading_level}"
                ),
            ),
        ],
    )

    llm_response = json.loads(llm_response)
    parsed_story = parse_llm_response(llm_response)
    return parsed_story


def generate_story_image(image_description: str):
    client = AzureOpenAI(
        api_version="2024-02-01",
        azure_endpoint="https://devan-m2gfjbpu-australiaeast.openai.azure.com",
        api_key="01bf290baa3140eda4340d8b8fb5920e",
    )

    print("starting call for image")
    res = client.images.generate(model="dall-e-3", prompt=image_description, n=1)

    image_url = json.loads(res.model_dump_json())["data"][0]["url"]
    print(image_url)
    return image_url


def generate_story_image_hyperbolic(image_description: str):
    url = "https://api.hyperbolic.xyz/v1/image/generation"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYWhlc2hzdW51d2FyNDQ3QGdtYWlsLmNvbSIsImlhdCI6MTcyOTM2NzUwMn0.jTZkGUR-Tenr6bsIf93OODCcsprYMCh_wggfpatKnE0",
    }
    data = {
        "model_name": "SDXL1.0-base",
        "prompt": image_description,
        "steps": 30,
        "cfg_scale": 5,
        "enable_refiner": False,
        "height": 400,
        "width": 400,
        "backend": "auto",
    }
    response = requests.post(url, headers=headers, json=data)
    print(len(response.json()["images"][0]["image"]))
    return response.json()["images"][0]["image"]
