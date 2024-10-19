from aesop.backend.llm import LLMApi, LLMModel
from aesop.backend.llm.prompts import STORY_GENERATION
from aesop.models import LLMMessage
from config import config


def generate_story(
    character_description: str, story_description: str, reading_level: str
):
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

    return llm_response


def generate_story_image(image_description: str):
    llm_api = LLMApi(
        model=LLMModel.GROQ_LLAMA_70B, api_key=config.llm_config.qrok_api_key
    )

    res = llm_api.generate_image(prompt=image_description)
    return res
