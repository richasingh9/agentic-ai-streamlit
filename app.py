
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import load_tools

st.title("Agentic AI Demo")

llm = ChatOpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

query = st.text_input("Ask something...")

if query:
    with st.spinner("Thinking..."):
        response = agent.run(query)
        st.write("🤖", response)
