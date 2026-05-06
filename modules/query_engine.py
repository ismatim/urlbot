"""Module for querying indexed Website data."""

# https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval//

import logging
from typing import Any, Dict, Optional

from llama_index.core import VectorStoreIndex, PromptTemplate

from modules.llm_interface import create_openai_llm
import config

logger = logging.getLogger(__name__)


def generate_initial_facts(index: VectorStoreIndex) -> str:
    """Generates interesting facts about the website\'s.

    Args:
        index: VectorStoreIndex containing the Website data.

    Returns:
        String containing interesting facts about the person.
    """
    try:
        # Create LLM for generating facts
        openai_llm = create_openai_llm(temperature=0.0, max_tokens=500)

        # Create prompt template
        facts_prompt = PromptTemplate(template=config.INITIAL_FACTS_TEMPLATE)

        # Create query engine
        query_engine = index.as_query_engine(
            streaming=False,
            similarity_top_k=config.SIMILARITY_TOP_K,
            llm=openai_llm,
            text_qa_template=facts_prompt,
        )

        # Execute the query
        query = "Provide three interesting facts about this website."
        response = query_engine.query(query)

        # Return the facts
        return response.response
    except Exception as e:
        logger.error(f"Error in generate_initial_facts: {e}")
        return "Failed to generate initial facts."


def answer_user_query(index: VectorStoreIndex, user_query: str) -> Any:
    """Answers the user's question using the vector database and the OpenAI LLM.

    Args:
        index: VectorStoreIndex containing the Website data.
        user_query: The user's question.

    Returns:
        Response object containing the answer to the user's question.
    """
    try:
        # Create OpenAI LLM instead
        # We use temperature=0.0 and max_tokens (OpenAI standard)
        openai_llm = create_openai_llm(temperature=0.0, max_tokens=250)

        # Create prompt template
        question_prompt = PromptTemplate(template=config.USER_QUESTION_TEMPLATE)

        # Create query engine
        # We pass the openai_llm here. LlamaIndex handles the prompt
        # augmentation (RAG) behind the scenes.
        query_engine = index.as_query_engine(
            streaming=False,
            similarity_top_k=config.SIMILARITY_TOP_K,
            llm=openai_llm,
            text_qa_template=question_prompt,
        )

        # 4. Execute the query
        # This one call embeds the query, finds matches in the index,
        # and sends it to GPT.
        answer = query_engine.query(user_query)

        return answer

    except Exception as e:
        logger.error(f"Error in answer_user_query: {e}")
        return "Failed to get an answer."
