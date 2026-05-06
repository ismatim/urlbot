"""Main script for running the URL Bot."""

import sys
import time
import logging
import argparse

from modules.data_extraction import extract_website
from modules.data_processing import (
    split_data,
    create_vector_database,
    verify_embeddings,
)
from modules.query_engine import generate_initial_facts, answer_user_query
from dotenv import load_dotenv


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout)],
)

logger = logging.getLogger(__name__)

load_dotenv()


def process_url(url):
    """
    Processes a URL, extracts data from the url, and interacts with the user.

    Args:
        url: The URL to extract or load mock data from.
        mock: If True, loads mock data from a premade JSON file instead of using the API.
    """
    try:
        # Extract the url data
        data = extract_website(url)

        if not data:
            logger.error("Failed to retrieve data.")
            return

        # Split the data into nodes
        nodes = split_data(data)

        # Store in vector database
        vectordb_index = create_vector_database(nodes)

        if not vectordb_index:
            logger.error("Failed to create vector database.")
            return

        # Verify embeddings
        if not verify_embeddings(vectordb_index):
            logger.warning("Some embeddings may be missing or invalid.")

        # Generate and display the initial facts
        initial_facts = generate_initial_facts(vectordb_index)

        print("\nHere are interesting facts about the website:")
        print(initial_facts)

        # Start the chatbot interface
        chatbot_interface(vectordb_index)

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")


def chatbot_interface(index):
    """
    Provides a simple chatbot interface for user interaction.

    Args:
        index: VectorStoreIndex containing the website data.
    """
    print(
        "\nYou can now ask more in-depth questions about this person. Type 'exit', 'quit', or 'bye' to quit."
    )

    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye!")
            break

        print("Bot is typing...", end="")
        sys.stdout.flush()
        time.sleep(1)  # Simulate typing delay
        print("\r", end="")

        response = answer_user_query(index, user_query)
        print(f"Bot: {response.response.strip()}\n")


def main():
    """Main function to run the URL Bot."""
    parser = argparse.ArgumentParser(description="Url Bot - Website Profile Analyzer")
    parser.add_argument("--url", type=str, help="Website URL")
    parser.add_argument(
        "--model",
        type=str,
        help='LLM model to use (e.g., "gpt-3.5-turbo")',
    )

    args = parser.parse_args()

    # Use command line arguments or prompt user for input
    url = args.url or input("Enter Website URL: ")

    if args.model:
        from modules.llm_interface import change_llm_model

        change_llm_model(args.model)

    # Use a default URL for mock data if none provided
    if not url:
        url = "https://www.ismaeltisminetzky.xyz/resume"

    process_url(url)


if __name__ == "__main__":
    main()
