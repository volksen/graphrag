# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License
"""A mock LLM that returns the given responses."""

from dataclasses import dataclass
from typing import Any

from fnllm import LLM, LLMInput, LLMOutput
from fnllm.types.generics import THistoryEntry, TJsonModel, TModelParameters
from typing_extensions import Unpack


@dataclass
class ContentResponse:
    """A mock content-only response."""

    content: str


class MockChatLLM(LLM):
    """A mock LLM that returns the given responses."""

    def __init__(self, responses: list[str]):
        self.responses = responses
        self.response_index = 0

    async def __call__(
        self,
        prompt: str,
        **kwargs: Unpack[LLMInput[TJsonModel, THistoryEntry, TModelParameters]],
    ) -> LLMOutput[Any, TJsonModel, THistoryEntry]:
        """Return the next response in the list."""
        response = self.responses[self.response_index % len(self.responses)]
        self.response_index += 1
        return LLMOutput(output=ContentResponse(content=response))