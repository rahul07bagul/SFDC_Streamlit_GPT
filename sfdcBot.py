import streamlit as st
import os

from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import constants

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

# Load the CSV files from data folder
@st.cache_resource(show_spinner=False)
def loadData():
    if PERSIST and os.path.exists("persist"):
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        #loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
        loader = DirectoryLoader("data/")
    if PERSIST:
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])
    return index

# Connect to OpenAI
def init():
    #st.set_page_config(page_title="Chat with the the Salesforce Data", layout="centered", initial_sidebar_state="auto", menu_items=None)
    os.environ["OPENAI_API_KEY"] = constants.APIKEY
    st.title("Chat with the Salesforce Data")

    if "messages" not in st.session_state.keys(): # Initialize the chat messages history
        st.session_state.messages = [
            {"role": "assistant", "content": "Ask me a question about your Salesforce Data"}
        ]

# Start Chatting with bot
def chat():
    init()
    index = loadData()

    chain = ConversationalRetrievalChain.from_llm(
      llm=ChatOpenAI(model="gpt-3.5-turbo"),
      retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    chat_history = []
    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Finding..."):
                response = chain({"question": prompt, "chat_history": chat_history})
                st.write(response['answer'])
                message = {"role": "assistant", "content": response['answer']}
                st.session_state.messages.append(message) # Add response to message history
                chat_history.append((prompt, response['answer']))