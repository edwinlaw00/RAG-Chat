from typing import List, Tuple
from vectordb import VectorDB
from util_ai import get_llm_response 
from util_str import format_references, get_chat_history_text
import os
import config

class ChatBot:
    def respond(chatbot: List, message: str, llm_type: str, temperature: float = 0.0) -> Tuple:
        if os.path.exists(config.VECTORDB_DIRECTORY):
            vectordb = VectorDB(config.VECTORDB_DIRECTORY)
        else:
            chatbot.append((message, f"VectorDB does not exist. Please first execute the 'upload_data_manually.py' module."))
            return "", chatbot, None

        print("Searching vectorDB for:", message)
        docs = vectordb.perform_similarity_search(message)
        retrieved_content = format_references(docs)

        # Construct prompt
        question = "# User new question:\n" + message
        chat_history = f"Chat history:\n {str(chatbot[-config.NUMBER_QA_PAIRS:])}\n\n"
        prompt = f"{chat_history}{retrieved_content}{question}"

        # Get response from LLM
        response_content = get_llm_response(llm_type, prompt, temperature)
        chatbot.append((message, response_content))

        # Construct chat history for display
        chat_history_text = get_chat_history_text(chatbot)
        
        return "", chatbot, retrieved_content, chat_history_text

