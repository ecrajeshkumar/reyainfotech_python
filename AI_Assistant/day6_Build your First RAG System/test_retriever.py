from retriever import retrieve

filename, content = retrieve("Artificial")

if filename and content:
    print(f"Found in file: {filename}")
    print(f"Content: {content}")
else:
    print("No relevant documents found.")
