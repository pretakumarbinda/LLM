import {config} from "dotenv";
config();

import {ChatGoogleGenerativeAI} from "@langchain/google-genai";
import { LLMChain } from "langchain/chains";
import {PromptTemplate} from "@langchain/core/prompts";

// 1. setup the model
const model = new ChatGoogleGenerativeAI({
    model: "models/gemini-2.5-flash",
    maxOutputTokens: 2048,
    temperature: 0.7,
    apiKey: process.env.GOOGLE_API_KEY,
});

// 2. create a prompt
const prompt = PromptTemplate.fromTemplate(
    "Explain the concept of {topic} to a begineer."
);

// 3. Build a chain
const chain = new LLMChain({
    llm: model,
    prompt: prompt,
})

// 4. Run it
const res = await chain.run("qunatum computing");
console.log("Gemini Response:\n",res);