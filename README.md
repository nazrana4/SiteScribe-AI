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
1. **Start the Application**:
   - Run the Python script.
   - Choose between scraping a website or querying content:
     ```bash
     1. Scrap a site
     2. Query documents
     3. Exit
     ```

2. **Scraping Websites**:
   - Enter the URL of the website to scrape.
   - The program will:
     - Fetch and save the HTML.
     - Parse and clean the content.
     - Save the cleaned content in the `./content` folder.

3. **Querying Content**:
   - Run the chatbot.Enter a query.
   - The chatbot retrieves relevant content and answers your query.

4. **Conversation History**:
   - The chatbot maintains a conversation log to provide context-aware responses.
   - Logs are saved persistently for future reference.

---


## **Future Improvements**
1. **Web Interface**:
   - Create a GUI for users to interact with the scraper and chatbot.
2. **Scalability**:
   - Use persistent databases like FAISS or Pinecone for large-scale document embeddings.

---
