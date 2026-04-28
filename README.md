# URL Bot

An AI-powered tool that generates personalized bot and conversation starters based on url. This project uses OpenAI and LlamaIndex.

## Project Overview

This AI url bot does the research for you. You input a name, and within seconds, the bot searches the url, generating personalized questions based on someo website.

## Features

- Extract URL data using `trafilatura` API.
- Process and index the data using LlamaIndex and OpenAI embeddings
- Generate interesting facts about the website
- Answer specific questions about the url.
- Interact with the bot through a command-line interface

## Project Structure

```
url_bot/
├── requirements.txt           # Dependencies
├── config.py                  # Configuration settings
├── modules/
│   ├── __init__.py
│   ├── data_extraction.py     # Url data extraction
│   ├── data_processing.py     # Data splitting and indexing
│   ├── llm_interface.py       # LLM setup and interaction
│   └── query_engine.py        # Query processing and response generation
└── main.py                    # Main script to run without Gradio
```

## Getting Started

### Prerequisites

- Python 3.11+
- OpenAI API Key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ismatim/urlbot.git
cd urlbot
```

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

1. Add your ProxyCurl API key to `config.py` (optional)

### Usage

#### Command Line Interface

Run the bot using the command line:

```bash
python main.py --mock  # Use mock data
# OR
python main.py --url "https://www.linkedin.com/in/username/" --api-key "your-api-key"
```

## Development Tasks

This is a starter template with placeholder functions. Your task is to implement the following components:

1. In `config.py`:
   - Define the prompt templates for facts generation and question answering

2. In `modules/data_extraction.py`:
   - Implement the `extract_website` function

3. In `modules/data_processing.py`:
   - Implement the `split_data` function
   - Implement the `create_vector_database` function
   - Implement the `verify_embeddings` function

4. In `modules/llm_interface.py`:
   - Implement the `create_openai_embedding` function
   - Implement the `create_openai_llm` function
   - Implement the `change_llm_model` function

5. In `modules/query_engine.py`:
   - Implement the `generate_initial_facts` function
   - Implement the `answer_user_query` function

6. Update `modules/__init__.py` to import your implemented functions

7. In `main.py`:
   - Implement the `process_url` function
   - Implement the `chatbot_interface` function

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Openai for providing the LLM and embedding models
- LlamaIndex for the data indexing and retrieval framework
