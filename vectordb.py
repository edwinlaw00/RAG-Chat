from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.vectorstores.chroma import Chroma
from util_ai import get_embedding_model
from typing import List
import os
import shutil
import config

class VectorDB:
    def __init__(self, path):
        self.path = path
    
    def __chunk_documents(self, docs: List) -> List:
        print("Chunking documents...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )
        chunked_documents = text_splitter.split_documents(docs)
        
        for chunk in chunked_documents:
            print(chunk.metadata)

        print("Number of chunks: {len(chunked_documents)}")
        return chunked_documents

    def save_to_vectordb(self, docs: list[Document]):
        if len(docs) <= 0:
            print("No documents to chunk")
        else:
            # Delete existing the database if needed
            if config.CREATE_NEW_VECTORDB and os.path.exists(self.path):
                shutil.rmtree(self.path)

            chunks = self.__chunk_documents(docs)
            embedding = get_embedding_model()

            print("Saving embeddings into", self.path, " ...")
            vectordb = Chroma.from_documents(
                documents=chunks,
                embedding=embedding,
                persist_directory=self.path
            )
            print(f"Number of embeddings created in vectordb: {vectordb._collection.count()}")
    
    def perform_similarity_search(self, message):
        embedding_model = get_embedding_model()
        vectordb = Chroma(persist_directory=self.path, embedding_function=embedding_model)
        return vectordb.similarity_search(message, k=config.K)
