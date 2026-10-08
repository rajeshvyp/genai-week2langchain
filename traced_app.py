from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
prompts = ["Explain Artificial intelligence in simple term.","What is RAG in Genertive AI?",
           "Explain LangSmith in simple term."]
for p in prompts:
    print(llm.invoke(p).content)