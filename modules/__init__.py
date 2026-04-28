"""
Url Bot modules package.

This package contains the following modules:
- data_extraction: Functions for extracting website data
- data_processing: Functions for processing and indexing Website data
- llm_interface: Functions for interfacing with OpenAI LLMs
- query_engine: Functions for querying indexed website data
"""

from modules.data_extraction import extract_website
from modules.data_processing import (
    split_data,
    create_vector_database,
    verify_embeddings,
)
from modules.llm_interface import (
    create_openai_embedding,
    create_openai_llm,
    change_llm_model,
)
from modules.query_engine import generate_initial_facts, answer_user_query
