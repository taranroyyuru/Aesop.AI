from chromadb import Documents, EmbeddingFunction, Embeddings
import chromadb
import chromadb.utils.embedding_functions as embedding_functions


client = chromadb.PersistentClient(path="/path/to/save/to")
	


def add_document_embeddings(document:str):
	# TODO: get api key from google and load from env
	google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key="YOUR_API_KEY")
	collection = client.client.get_or_create_collection(name="stories", embedding_function=google_ef)
	collection.add_document(document)


