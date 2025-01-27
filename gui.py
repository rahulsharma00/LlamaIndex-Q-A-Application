import os.path
from dotenv import load_dotenv
import streamlit as st
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# Load environment variables from the .env file
load_dotenv('/Users/rahulsharma/Desktop/rag llm/.env')

# Define storage directory
PERSIST_DIR = "./storage"

# Load or create the index
@st.cache_resource
def get_index():
    if not os.path.exists(PERSIST_DIR):
        # Load documents and create index
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # Load existing index from storage
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    return index

# Initialize the index
index = get_index()

# Streamlit UI
st.title("LlamaIndex Q&A Application")
st.write("Ask any question based on the indexed documents.")

# Input field for user query
user_query = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_query.strip():
        query_engine = index.as_query_engine()
        response = query_engine.query(user_query)
        st.subheader("Answer:")
        st.write(response.response)
    else:
        st.warning("Please enter a question before submitting.")

st.sidebar.title("Instructions")
st.sidebar.write("""
1. Enter your question in the input field.
2. Click the **Submit** button to get an answer.
3. Ensure your documents are in the 'data' directory for processing.
""")
