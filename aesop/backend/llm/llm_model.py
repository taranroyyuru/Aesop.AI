"""
llm_model - Enum for LLM models.

This module provides the LLMModel enumeration for various models of
Large Language Models (LLMs), enabling dynamic management of model sources.
"""

from enum import Enum

from .llm_provider import LLMProvider


class LLMModel(Enum):
    """Enum for LLM models."""

    GPT_4 = ("gpt-4", LLMProvider.OPENAI)
    GPT_4O_MINI = ("gpt-4o-mini", LLMProvider.OPENAI)
    GPT_3_5_TURBO = ("gpt-3.5-turbo", LLMProvider.OPENAI)
    GEMINI_1_5_PRO = ("gemini/gemini-1.5-flash", LLMProvider.GEMINI)
    GEMINI_1_5_FLASH = ("gemini/gemini-1.5-flash", LLMProvider.GEMINI)
    CLAUDE_3_5_SONNET = ("claude-3-5-sonnet-20240620", LLMProvider.ANTHROPIC)
    CLAUDE_3_HAIKU = ("claude-3-haiku-20240307", LLMProvider.ANTHROPIC)
    GROQ_LLAMA_70B = ("groq/llama-3.1-70b-versatile", LLMProvider.GROQ)

    def __init__(self, model_name: str, provider: LLMProvider):
        self.model_name = model_name
        self.provider = provider

    @classmethod
    def from_model_name(cls, model_name: str):
        """Convert a model name string to a Model enum instance."""
        for model in cls:
            if model.model_name == model_name:
                return model
        raise ValueError(f"No Model found for model_name: {model_name}")
