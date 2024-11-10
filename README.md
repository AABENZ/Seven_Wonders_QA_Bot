# Seven Wonders QA Bot

A question-answering system about the Seven Wonders of the World, built using Chainlit, Haystack, and OpenAI.

## Project Overview

This project is a conversational AI system that answers questions about the Seven Wonders of the World. The system uses a combination of natural language processing (NLP) and machine learning algorithms to retrieve relevant information from a dataset and generate human-like responses.


![App Screenshot](https://i.ibb.co/YdBn8sw/2024-11-10-23-53.png)



## Features

- **Question Answering**: The system can answer questions about the Seven Wonders of the World, including their history, location, and significance.
- **Conversational Interface**: The system uses a conversational interface to interact with users, making it easy to ask questions and receive answers.
- **Knowledge Retrieval**: The system uses a knowledge retrieval algorithm to retrieve relevant information from a dataset and generate responses.

## Technical Details

- **Framework**: Chainlit
- **NLP Library**: Haystack
- **Machine Learning Model**: OpenAI GPT-4
- **Dataset**: Seven Wonders of the World dataset
- **Programming Language**: Python

## Prerequisites

- Python 3.8+
- OpenAI API Key

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/ask_multiple_pdfs.git
   cd ask_multiple_pdfs

2. **Create a Virtual Environment**:

   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**:

   ```bash
    pip install -r requirements.txt

2. **Set Up API Keys**:

   ```bash
    OPENAI_API_KEY=your_openai_api_key_here

### Running the Application

**To start the Chainlit app, run**:

```bash
chainlit run app.py