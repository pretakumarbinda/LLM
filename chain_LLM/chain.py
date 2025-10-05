from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# import and setup the MODEL
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# create Gemini model
model = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature =0.7,
    max_output_tokens=2048,
    google_api_key=api_key
    
)

#Create the prompt
prompt = PromptTemplate.from_template("Explain the concept of {topic} to a begineer.")

#Build chain
chain=LLMChain(
    llm=model,
    prompt=prompt
)

response = chain.run("quantum computing")
print("Gemini Response:\n",response)