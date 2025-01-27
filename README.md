# LlamaIndex-Q-A-Application
This repository provides an easy-to-use framework for indexing and querying documents with the LlamaIndex library. By following the structure of this code, users can create their own Q&A system that indexes documents, persists the index for later use, and performs efficient querying.

## Note 
Create a folder named 'data' and place your PDF files inside it. The 'storage' folder will store the indexed data for later use. 

### Code Explanation: LlamaIndex Q&A Application

This Python code is designed to create a **Question & Answer** system using **LlamaIndex** and **Streamlit**. The system works by indexing a set of documents and then allowing users to query the index for relevant information.

Here’s a breakdown of the key components:

1. **Loading Environment Variables**:  
   The code begins by importing necessary modules and loading the environment variables from a `.env` file using the `python-dotenv` library. The `load_dotenv()` function ensures that environment variables (like API keys or file paths) are available to the app.

   ```python
   from dotenv import load_dotenv
   load_dotenv('/Users/rahulsharma/Desktop/rag llm/.env')
   ```

2. **Setting Up the Index**:  
   The **LlamaIndex** library is used to process documents. The `VectorStoreIndex` stores the document data in a vector format, which allows for efficient querying. The **SimpleDirectoryReader** is used to read the documents from the "data" directory.

   - If the index doesn't already exist, the documents are read, and an index is created.
   - If the index already exists (i.e., stored in the `./storage` directory), it loads the existing index for querying.

   ```python
   if not os.path.exists(PERSIST_DIR):
       documents = SimpleDirectoryReader("data").load_data()
       index = VectorStoreIndex.from_documents(documents)
       index.storage_context.persist(persist_dir=PERSIST_DIR)
   else:
       storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
       index = load_index_from_storage(storage_context)
   ```

3. **Querying the Index**:  
   Once the index is loaded (either created or retrieved), it is ready to be queried. The `query_engine` object is created using the index, and a sample query ("What are transformers?") is processed. The response from the query is printed.

   ```python
   query_engine = index.as_query_engine()
   response = query_engine.query("What are transformers?")
   print(response)
   ```

4. **Flexibility and Persistence**:  
   The system is designed to store the index in a persistent directory (`./storage`) so that it doesn’t need to be recreated every time the application runs. This allows users to add more documents or make changes to the index without starting from scratch.

---

![image](https://github.com/user-attachments/assets/9e7a7fe3-8f57-4154-adf9-e936c96b64eb) 

