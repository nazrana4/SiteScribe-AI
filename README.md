# SiteScribe-AI

## **Project Overview**
This project aims to scrape websites, extract and clean their content, and answer user queries based on the scraped data. Additionally, it integrates a chatbot capable of retaining conversation history for contextual and seamless interactions.

---

## **Features Implemented**

### 1. **Web Scraping**
- **HTML Fetching**: Fetches the HTML content of a given website using the `requests` library.
- **File Handling**:
  - Avoids redundant downloads by checking if the file already exists.
- **Content Cleaning**:
  - Parses and cleans the HTML content using `BeautifulSoup`.
  - Removes unnecessary whitespace and extracts meaningful text.
- **Output Storage**:
  - Saves the cleaned content to a separate folder (`./content`) with the page title as the filename.

### 2. **Language Model Integration**
- **LLM-Based Querying**:
  - Integrates an OpenAI-compatible model for answering questions.
  - Accepts user queries and returns responses based on the provided context.
- **Custom Embeddings**:
  - Uses `SentenceTransformer` for document embeddings.
  - Supports semantic similarity searches within the scraped content.

### 3. **Retrieve-and-Answer (RAG) Pipeline**
- Retrieves relevant chunks of content based on user queries.
- Answers questions using context retrieved from the vector store.
- Provides concise and grounded answers or acknowledges if the answer is unavailable.

### 4. **Chatbot with Conversation History**
- Maintains conversation history to ensure context-aware responses.
- Provides users with a natural, chat-like interface for interactions.

---

## **How to Use**

### **Prerequisites**
- Python 3.8+
- Install the required Python libraries:
  ```bash
  pip install requests beautifulsoup4 lxml sentence-transformers langchain-community langchain-core langchain-google-vertexai
  ```

### **Steps to Run**
1. **Scraping Websites**:
   - Run the python script (scrapper.py).
   - Enter the URL of the website to scrape.
   - The program will:
     - Fetch and save the HTML.
     - Parse and clean the content.
     - Save the cleaned content in the `./content` folder.
     - Upload the scraped contents in this folder to google drive.

2. **Querying Content**:
   - Run the app.ipynb in Google Collab and install the dependencies.
   - Mount the google drive and access the content stored on the drive.
   - Then run the cells in the notebook.
   - Input the query making call to the function rag_call_with_history passing your query as the parameter.
   - The chatbot retrieves relevant content and answers your query.

3. **Conversation History**:
   - The chatbot maintains a conversation history for context-aware responses.
---


## **Future Improvements**
1. **Web Interface**:
   - Create a GUI for users to interact with the scraper and chatbot.
2. **Improved Chat History**:
   - Using hybrid technique for keeping the chat history. We can combine condensed plus summarized history for effeciency.
4. **Scalability**:
   - Use persistent databases like FAISS or Pinecone for large-scale document embeddings.

---
