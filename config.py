"""Configuration settings for the Url Bot."""

# Model settings
LLM_MODEL_ID = "gpt-4o-mini"
EMBEDDING_MODEL_ID = "text-embedding-3-small"

# ProxyCurl API settings
PROXYCURL_API_KEY = ""  # Replace with your API key

# Query settings
SIMILARITY_TOP_K = 5
TEMPERATURE = 0.1
MAX_NEW_TOKENS = 500
MIN_NEW_TOKENS = 1
TOP_K = 50
TOP_P = 1

# Node settings
CHUNK_SIZE = 500

# LLM prompt templates
INITIAL_FACTS_TEMPLATE = """
You are an AI assistant that provides detailed answers based on the provided context.

Context information is below:

{context_str}

Based on the context provided, create summary of this website.

Answer in detail, using only the information provided in the context.
"""

USER_QUESTION_TEMPLATE = """
You are an AI assistant that provides detailed answers to questions based on the provided context.

Context information is below:

{context_str}

Question: {query_str}

Answer in full details, using only the information provided in the context. If the answer is not available in the context, say "I don't know. The information is not available on the page."
"""
