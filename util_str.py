from typing import List
import re
import ast
import html
import os

def get_date_from_filename(filename):
    # Define the regex pattern for matching timestamps
    pattern = r"(\b\d{4})-?(\d{2})-?(\d{2})-?(\d{0,4})\b"

    # Search for the pattern in the filename
    match = re.search(pattern, filename)

    # If match is found, extract year, month, and date
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        
        if year is not None:
            if month is not None:
                if day is not None:
                    return f"[Date: {year}-{month}-{day}] "
                else:
                    return f"[Date: {year}-{month}] "
            else:
                return f"[Date: {year}] "    
    else:
        return ''
    
def format_references(documents: List) -> str:
    documents = [str(x)+"\n\n" for x in documents]
    markdown_documents = ""
    counter = 1
    
    for doc in documents:
        # Extract content and metadata
        content, metadata = re.match(r"page_content=(.*?)( metadata=\{.*\})", doc).groups()
        metadata = metadata.split('=', 1)[1]
        metadata_dict = ast.literal_eval(metadata)

        # Decode newlines and other escape sequences
        content = bytes(content, "utf-8").decode("unicode_escape")

        # Replace escaped newlines with actual newlines
        content = re.sub(r'\\n', '\n', content)
        # Remove special tokens
        content = re.sub(r'\s*<EOS>\s*<pad>\s*', ' ', content)
        # Remove any remaining multiple spaces
        content = re.sub(r'\s+', ' ', content).strip()

        # Decode HTML entities
        content = html.unescape(content)

        # Replace incorrect unicode characters with correct ones
        content = content.encode('latin1').decode('utf-8', 'ignore')

        # Remove or replace special characters and mathematical symbols
        # This step may need to be customized based on the specific symbols in your documents
        content = re.sub(r'â', '-', content)
        content = re.sub(r'â', '∈', content)
        content = re.sub(r'Ã', '×', content)
        content = re.sub(r'ï¬', 'fi', content)
        content = re.sub(r'â', '∈', content)
        content = re.sub(r'Â·', '·', content)
        content = re.sub(r'ï¬', 'fl', content)

        # Append cleaned content to the markdown string with two newlines between documents    
        markdown_documents += f"# Retrieved content {counter}:\n" + content + "\n\n" + \
            f"Source: {os.path.basename(metadata_dict['source'])}" + " | " +\
            f"Page number: {str(metadata_dict['page'])}" + "\n\n"
        counter += 1

    return markdown_documents

def get_chat_history_text(chat_history) -> str:
    chat_history_text = ''
    chat_history_text_prompt = "You"
    for qa_pair in chat_history:
        for line in qa_pair:
            chat_history_text += f"{chat_history_text_prompt}: {line}\n\n"
            if (chat_history_text_prompt == "You"):
                chat_history_text_prompt = "Bot"
            else:
                chat_history_text_prompt = "You"     
                    
    return chat_history_text