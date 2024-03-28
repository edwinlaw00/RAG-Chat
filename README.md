# RAG-Chat
This is a simple configurable GTP-style chatbot built on RAG architecture. I built it with highly configurable and extensible modules in mind.

My inpsiration originally came from this other project:
[LLM-Zero-to-Hundred/RAG-GPT at master · Farzad-R/LLM-Zero-to-Hundred](https://github.com/Farzad-R/LLM-Zero-to-Hundred/tree/master/RAG-GPT)

## Architecture Overview
Coming...

## Instructions
1. Clone GIT respository
2. Initiate Python environment
    ```
    python3 -m venv .
    ```
3. Install required python libraries
    ```
    bin/pip install -r requirements.txt
    ```
4. Modify configuration file `config.py`

5. Setup OpenAI key (if you want to use OpenAI APIs)
    ```
    export OPENAI_API_KEY=<OpenAI Key>
    ```
    _where <OpenAI Key> is your OpenAI access key_

6. Start Ollama LLM (if you want to use local LLMs)

7. Create vector database from documents
    ```
    bin/python3 create_database.py 
    ```
8. Run app
    ```
    bin/python3 ragchat.py 
    ```

### Configuration Settings
Coming...