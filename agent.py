from langchain.agents import Tool, initialize_agent
from langchain.llms import Ollama
from tools import load_data
lm=Ollama(model="llama3")
tools=[Tool(name="LoadData" ,func=load_data,description="Load csv from a path")]
agent=initialize_agent(tools=,llm,agent="zero-shot-react-decription",verbose=True)

user_query=input("enter yout data analysis request:")
agent.run(user_query)