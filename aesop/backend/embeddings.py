from chromadb import Documents, EmbeddingFunction, Embeddings
import chromadb
import chromadb.utils.embedding_functions as embedding_functions
from dotenv import load_dotenv
import os

load_dotenv()


def add_document_embeddings(*docs:str):
	# TODO: get api key from google and load from env
	client = chromadb.HttpClient(host='localhost', port=8000)
	google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=os.getenv("GEMINI_KEY"))
	collection = client.get_or_create_collection(name="stories", embedding_function=google_ef)

	collection.add(documents=list(docs), ids = [str(hash(document)) for document in docs])
	return collection.count()

def get_document_embeddings(*documents:str):
	client = chromadb.HttpClient(host='localhost', port=8000)
	google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=os.getenv("GEMINI_KEY"))
	collection = client.get_or_create_collection(name="stories", embedding_function=google_ef)


	return collection.query(
    query_texts=list(documents),
    n_results=10,
    where={"metadata_field": "is_similar_to_this"},
    where_document={"$contains":"search_string"}
)