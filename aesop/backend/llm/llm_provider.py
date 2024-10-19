"""
llm_provider - Enum for LLM providers.

This module defines the LLMProvider enumeration for various providers of
Large Language Models (LLMs), enabling dynamic management of model sources.
"""

from enum import Enum


class LLMProvider(Enum):
    """Enum for LLM providers."""

    OPENAI = "openai"
    GEMINI = "gemini"
    ANTHROPIC = "anthropic"
    GROQ = "groq"
