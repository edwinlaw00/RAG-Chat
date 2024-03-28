# Directory paths
PRELOAD_DIRECTORY = 'data/doc'
VECTORDB_DIRECTORY = 'data/vectordb/chroma/'

# Embedding
#EMBEDDING_MODEL = 'text-embedding-ada-002'
EMBEDDING_MODEL = 'avsolatorio/GIST-Embedding-v0'

# VectorDB flags and parameters
CREATE_NEW_VECTORDB = True
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 500

# LLMs
llm_list = ["gpt-3.5-turbo", "mistral:instruct", "llama2:latest", "tinyllama"]
default_llm = "mistral:instruct"

# LLM prompt=
llm_system_role = """
    Here is some information including a chat history, some retrieved content and the source. 
    Your task is to respond to the user's new question using the information from the retrieved content.
    If no relevant information is found in the retreived content, say so. Do not use your own information.
    
    You will receive a prompt with the the following format:

    # Chat history:
    [user query, response]

    # Retrieved content number:
    Content
    Source

    # User new question:
    New question
    """
# Return K number of content from similarity search
K = 3

# Number of Q/A pairs preserved in chat history
NUMBER_QA_PAIRS = 2


  