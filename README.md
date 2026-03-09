# AI Knowledge Chatbot 🤖

An NLP-powered chatbot that answers questions using information from multiple text documents.
The chatbot uses **sentence embeddings and semantic similarity** to retrieve the most relevant answer from its knowledge base.

---

## 🚀 Features

* Conversational chatbot interface
* Semantic search using sentence embeddings
* Knowledge base from multiple `.txt` files
* Greeting, thanks, and goodbye detection
* Chat interface with Streamlit
* Session-based chat history
* Handles unknown questions with fallback response

---

## 🧠 Technologies Used

* Python
* NLTK
* Sentence Transformers
* Streamlit
* PyTorch

---

## 📂 Project Structure

```text
AI-Knowledge-Chatbot
│
├── app.py                # Main Streamlit chatbot application
├── README.md             # Project documentation
│
└── data/                 # Knowledge base used by the chatbot
    ├── artificial_intelligence.txt            # Artificial Intelligence concepts
    ├── machine_learning.txt
    ├── deep_learning.txt
    ├── natural_language_processing.txt           # Natural Language Processing topics
    └── python.txt        # Python programming concepts
```

### 📄 Description of Files

**app.py**
Main Python script that runs the chatbot interface and handles NLP processing.

**data/**
Folder containing knowledge documents. The chat


The **data folder** contains knowledge documents that the chatbot reads to answer questions.

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/yourusername/NLP-Chatbot.git
cd NLP-Chatbot
```

2. Install dependencies

```
pip install streamlit nltk sentence-transformers
```

3. Download NLTK resources

These will download automatically when the app runs.

---

## ▶️ Running the Application

Start the Streamlit app with:

```
streamlit run app.py
```

Then open the link shown in your terminal (usually):

```
http://localhost:8501
```

---

## 🧩 How the Chatbot Works

1. The chatbot loads `.txt` files from the **data folder**.
2. Text is split into sentences using **NLTK tokenization**.
3. Each sentence is converted into **vector embeddings** using the Sentence Transformer model `all-MiniLM-L6-v2`.
4. When a user asks a question:

   * The question is converted into an embedding.
   * Cosine similarity compares the question with all stored sentence embeddings.
5. The sentence with the highest similarity is returned as the answer.

---

## 💬 Example

User question:

```
What is machine learning?
```

Bot response:

```
Machine learning is a subset of artificial intelligence that enables systems to learn patterns from data without explicit programming.
```

---


## 📊 Limitations

* The chatbot retrieves answers from documents instead of generating new responses.
* Answers depend on the quality of the knowledge base.

---

## 🔮 Future Improvements

* PDF and web page knowledge sources
* Top-3 answer ranking
* Confidence score display
* Conversation context memory
* Wikipedia data integration

---

## 📚 Project Type

This is a **retrieval-based NLP chatbot** built using semantic search and sentence embeddings.

---

## 👨‍💻 Author

Haritha P

---

## ⭐ If you like this project

Consider giving the repository a star on GitHub!
