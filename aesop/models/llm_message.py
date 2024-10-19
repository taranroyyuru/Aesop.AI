"""
llm_message - Model representing a message for LLM interaction.
"""

from typing import Literal

from pydantic import BaseModel, Field


class LLMMessage(BaseModel):
    """Model representing a message for LLM interaction."""

    role: Literal["user", "assistant", "system"]
    content: str = Field(..., description="The content of the message")
