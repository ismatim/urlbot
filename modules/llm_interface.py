"""Module for interfacing with OpenAI LLMs."""

import logging
import os
from typing import Dict, Any, Optional

# Switch imports to OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI

import config

logger = logging.getLogger(__name__)


def create_openai_embedding() -> OpenAIEmbedding:
    """Creates an OpenAI Embedding model for vector representation.

    Returns:
        OpenAIEmbedding model.
    """
    # OpenAI looks for OPENAI_API_KEY .env
    openai_embedding = OpenAIEmbedding(
        model=config.EMBEDDING_MODEL_ID,  # "text-embedding-3-small"
    )
    logger.info(f"Created OpenAI Embedding model: {config.EMBEDDING_MODEL_ID}")
    return openai_embedding


def create_openai_llm(
    temperature: float = config.TEMPERATURE,
    max_tokens: int = config.MAX_NEW_TOKENS,
) -> OpenAI:
    """Creates an OpenAI LLM for generating responses.

    Args:
        temperature: Temperature for controlling randomness (0.0 to 1.0).
        max_tokens: Maximum number of tokens to generate.

    Returns:
        OpenAI model.
    """
    # OpenAI uses 'max_tokens' instead of 'max_new_tokens'
    openai_llm = OpenAI(
        model=config.LLM_MODEL_ID,  # e.g., "gpt-4o" or "gpt-3.5-turbo"
        temperature=temperature,
        max_tokens=max_tokens,
    )
    logger.info(f"Created OpenAI LLM model: {config.LLM_MODEL_ID}")
    return openai_llm


def change_llm_model(new_model_id: str) -> None:
    """Change the LLM model to use.

    Args:
        new_model_id: New LLM model ID to use.
    """
    config.LLM_MODEL_ID = new_model_id
    logger.info(f"Changed LLM model to: {new_model_id}")
