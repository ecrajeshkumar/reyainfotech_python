from memory import (
    create_database,
    save_memory,
    search_semantic_memories
)


create_database()

save_memory(
    "My name is Rajesh.",
    "Nice to meet you, Rajesh."
)

save_memory(
    "I am learning Python.",
    "Python is useful for AI development."
)

save_memory(
    "I am learning about MCP.",
    "MCP allows AI applications to use tools."
)

save_memory(
    "What is capital of Bihar.",
    "Patna."
)

results = search_semantic_memories(
    "capital of India"
)

print("\nRelevant Memories")
print("-----------------")

for result in results:
    print("\nScore:", result["score"])
    print("User:", result["user_message"])
    print("Assistant:", result["assistant_message"])
