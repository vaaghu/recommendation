import chromadb

chroma_client = chromadb.PersistentClient(path="/home/vaaghu/programming/RAG/chroma")
collection = chroma_client.get_or_create_collection(
    name="first", metadata={"hnsw:space": "l2"}
)