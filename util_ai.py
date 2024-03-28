from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import config

def get_embedding_model():
    print("Embedding model:", config.EMBEDDING_MODEL)
    if config.EMBEDDING_MODEL.startswith('text-embedding-'):
        # OpenAI embedding models
        return OpenAIEmbeddings()
    else:
        # Otherwise assume embedding model available in Hugging Face
        return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
    
def get_llm_response(llm_name, prompt, temperature):
    prompt = f"{config.LLM_PROMPT}{prompt}"
    print(f"Prompt ========================\n{prompt}\n========================")
    print(f"Getting response from LLM '{llm_name}' with temperature {temperature}")

    if llm_name.startswith('gpt-'):
        # OpenAI LLM
        llm = ChatOpenAI(temperature=temperature, model_name=llm_name)
    else:
        # Assume local Ollama LLM avaiable
        llm = ChatOllama(temperature=temperature, model=llm_name)

    prompt_template = ChatPromptTemplate.from_template(prompt)
    chain = prompt_template | llm | StrOutputParser()
    return chain.invoke({})