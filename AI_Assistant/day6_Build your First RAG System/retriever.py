from pathlib import Path

def load_documents():
    # Load documents/files from the specified path
    documents = {}
    folder = Path("knowledge")
    for file in folder.glob('*.txt'):
        documents[file.name] = file.read_text(encoding='utf-8')
    return documents

def retrieve(query):
    # Retrieve relevant documents based on the query
    documents = load_documents()
    for filename, content in documents.items():
        if query.lower() in content.lower():
            return filename,content
    return None,None


