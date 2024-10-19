from chromadb import Documents, EmbeddingFunction, Embeddings
import chromadb
import chromadb.utils.embedding_functions as embedding_functions


client = chromadb.PersistentClient(path="localdata/")
google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key="YOUR_API_KEY")
collection = client.client.get_or_create_collection(name="stories", embedding_function=google_ef)


def add_document_embeddings(document:str):
	# TODO: get api key from google and load from env

	collection.add_document(document)

def get_document_embeddings(document:str):
	return collection.query(
    query_texts=["doc10", "thus spake zarathustra", ...],
    n_results=10,
    where={"metadata_field": "is_equal_to_this"},
    where_document={"$contains":"search_string"}
)