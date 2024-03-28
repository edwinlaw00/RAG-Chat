from documents import Documents
from vectordb import VectorDB
import config

def main():
    # Load documents
    documents = Documents(path=config.DOC_DIRECTORY).getDocuments()

    # Load documents into vector database    
    if len(documents) > 0:
        VectorDB(config.VECTORDB_DIRECTORY).save_to_vectordb(documents)
    
if __name__ == "__main__":
    main()