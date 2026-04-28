"""Module for extracting website."""

import time
import trafilatura
import logging
import sys
from typing import Dict, Optional, Any

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout)],
)

logger = logging.getLogger(__name__)


def extract_website(url: str):
    """Extracts website data from a website URL. Placeholder for future implementation.

    Args:
        url: The website URL to extract data from.
    """
    if not url:
        raise ValueError("url key is required.")

    logger.info("Starting to extract the url...")
    start_time = time.time()
    logger.info(f"Extracting data from website URL: {url}")
    # Placeholder for future implementation
    try:
        downloaded = trafilatura.fetch_url(url)

        # This returns just the main text, no HTML, no ads.
        result = trafilatura.extract(downloaded)
        logger.info(
            f"Extracted url content: {result}..."
        )  # Print first 200 chars of the result
        return result

    except Exception as e:
        logger.error(f"Error extracting website: {e}")

    logger.info(
        f"Sending API request to ProxyCurl at {time.time() - start_time:.2f} seconds..."
    )
    return {}
