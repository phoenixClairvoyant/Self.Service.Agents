import streamlit as st
from src.openai_react_agent import rag_docs
#from src.gemini_react_agent import rag_docs
import time

def main():
    st.title("Chat with React Agent")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is your question?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Measure execution time
        start_time = time.time()
        response = rag_docs(prompt)
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
            st.markdown(f"*Query execution time: {execution_time:.2f} seconds*")
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": f"{response}\n\n*Query execution time: {execution_time:.2f} seconds*"})

if __name__ == "__main__":
    main()
