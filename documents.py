from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from typing import List
from util_str import get_date_from_filename
import os

class Documents:
    def __init__(self, path=''):
        self.path = path
        self.docs = []

        # Load MD files
        self.docs.extend(self.__load_md_documents())
        
        # Load PDF files
        self.docs.extend(self.__load_pdf_documents())

        print(f"Total number of files loaded: {len(self.docs)}")
        
        # Add date (if available from filename)
        self.__add_date()
    
    def __load_md_documents(self) -> List:
        print("Loading Markdown documents from", self.path , "...")

        loader = DirectoryLoader(self.path, recursive=True, glob="*.md")
        docs = loader.load()

        # Treat the entire MD file as one page. Add page number 0
        for doc in docs:
            doc.metadata['page'] = 0
    
        print(f"Added {len(docs)} MD file(s).")
        return docs

    def __load_pdf_documents(self) -> List:
        print("Loading PDF documents from", self.path , "...")
        
        loader = DirectoryLoader(self.path, recursive=True, glob="*.pdf", loader_cls=PyPDFLoader)
        docs = loader.load()
        
        # One PDF file may contain multiple pages. They will be split into multiple docs.
        print(f"Added {len(docs)} PDF page(s).") 
        return docs

    def __add_date(self):
        for doc in self.docs:
            # Extract the filename from source
            filename = os.path.basename(doc.metadata['source'])
            date_str = get_date_from_filename(filename)
            if date_str is not None and len(date_str) > 0:
                print(f"Adding date info {date_str}to {filename}")
                doc.page_content = f"{date_str}{doc.page_content}"
    
    def getDocuments(self):
        return self.docs
