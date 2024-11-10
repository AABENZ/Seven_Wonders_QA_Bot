import chainlit as cl  # Framework for building chat interfaces
from datasets import load_dataset  # Hugging Face datasets library
from haystack.document_stores import InMemoryDocumentStore  # Document storage
from haystack.nodes import BM25Retriever  # Search/retrieval system
from haystack.pipelines import Pipeline  # Pipeline management
import os
from openai import OpenAI  # OpenAI API client
from dotenv import load_dotenv  # Environment variable management
from pathlib import Path


load_dotenv()

# Load dataset and initialize document store and retriever
dataset = load_dataset("bilgeyucel/seven-wonders", split="train")
document_store = InMemoryDocumentStore(use_bm25=True)
document_store.write_documents(dataset)
retriever = BM25Retriever(document_store=document_store, top_k=3)

# OpenAI API setup
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)



# Define the pipeline (retriever only, since OpenAI handles generation)
generative_pipeline = Pipeline()
generative_pipeline.add_node(component=retriever, name="retriever", inputs=["Query"])

@cl.on_chat_start
async def main():
    # Add startup message
    root_path = Path(__file__).parent
    default_chainlit_md_path = root_path / "chainlit.md"
    message = default_chainlit_md_path.read_text()
    startup_message = cl.Message(content=message)
    await startup_message.send()


@cl.on_message
async def handle_message(message: cl.Message):
    # Extract the text content from the message
    query_text = message.content
    
    # Retrieve documents relevant to the query
    retrieval_result = generative_pipeline.run(query=query_text)
    retrieved_docs = retrieval_result["documents"]

    # Prepare documents context for OpenAI API
    docs_text = "\n".join([doc.content for doc in retrieved_docs])
    prompt = f"""
    Answer the question truthfully based solely on the given documents. If the documents do not contain the answer to the question, say that answering is not possible given the available information. Your answer should be no longer than 50 words.
    Documents:
    {docs_text}
    Question: {query_text}
    Answer:
    """

    # Generate response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if available and preferred
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the response text
    answer = response.choices[0].message.content
    
    # Send the response to Chainlit
    await cl.Message(author="Bot", content=answer).send()
