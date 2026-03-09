import streamlit as st
import os
import nltk
import random

from sentence_transformers import SentenceTransformer, util

# download tokenizer
nltk.download('punkt')
nltk.download('punkt_tab')


# load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# ------------------------------
# Greeting, thanks, goodbye lists
# ------------------------------

greet_inputs = ("hello", "hi", "hey", "good morning", "good evening")
greet_responses = ["Hello!", "Hi there!", "Hey! How can I help you?"]

thanks_inputs = ("thanks", "thank you")
thanks_responses = ["You're welcome!", "Happy to help!", "Anytime!"]

bye_inputs = ("bye", "goodbye", "see you")

# ------------------------------
# Greeting function
# ------------------------------

def greet(sentence):
    for word in sentence.lower().split():
        if word in greet_inputs:
            return random.choice(greet_responses)

# ------------------------------
# Load TXT documents
# ------------------------------

def load_documents(folder):

    sentences = []

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            with open(os.path.join(folder,file),"r",encoding="utf-8") as f:

                text = f.read()

                sentences += nltk.sent_tokenize(text)

    return sentences


sentences = load_documents("data")

# create embeddings
sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

# ------------------------------
# Chatbot response function
# ------------------------------

def chatbot_response(user_query):

    # greetings
    greeting = greet(user_query)
    if greeting:
        return greeting

    # thanks
    if user_query.lower() in thanks_inputs:
        return random.choice(thanks_responses)

    # goodbye
    if user_query.lower() in bye_inputs:
        return "Goodbye! Have a great day."

    # semantic search
    query_embedding = model.encode(user_query, convert_to_tensor=True)

    similarity_scores = util.cos_sim(query_embedding, sentence_embeddings)

    best_match = similarity_scores.argmax()

    score = similarity_scores[0][best_match]

    # fallback if similarity too low
    if score < 0.3:
        return "Sorry, I couldn't find an answer in my knowledge base."

    return sentences[best_match]


# ------------------------------
# Streamlit Chat Interface
# ------------------------------

st.title("AI Knowledge Chatbot 🤖")

st.write("Ask questions about AI, Machine Learning, NLP, Deep Learning or Python.")

# session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# user input
user_input = st.chat_input("Ask a question")

if user_input:

    # add user message
    st.session_state.messages.append({"role":"user","content":user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # bot response
    bot_response = chatbot_response(user_input)

    st.session_state.messages.append({"role":"assistant","content":bot_response})

    with st.chat_message("assistant"):
        st.write(bot_response)