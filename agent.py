# A project demonstrating how to build a simple AI Web Agent that combines Google Gemini with SerpAPI (for real-time web search) using LangChain.
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool
from dotenv import load_dotenv
import os

load_dotenv()

#Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.7,
    max_output_tokens=2048,
    api_key=os.getenv("GOOGLE_API_KEY")
)

#Initialize SerpAPI
search = SerpAPIWrapper(
    serpapi_api_key=os.getenv("SERPAPI_API_KEY"),
)

#Wrap the SerpAPI function
search_tool = Tool(
    name="Web Search",
    func=search.run,
    description="Useful for searching current events or latest news."
)
# Create the agent
agent = initialize_agent(
    tools=[search_tool],
    llm=model,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run a query
query = "What is the latest news about ISRO?"
response = agent.run(query)

# Output
print("🛰️ Final Output:", response)

