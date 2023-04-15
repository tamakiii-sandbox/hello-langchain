import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 0
DEEPLAKE_PATH = os.environ['DEEPLAKE_API_KEY']

root_dir = './dependency/twitter/the-algorithm'
documents = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        try:
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            documents.extend(loader.load_and_split())
        except Exception as e:
            pass

text_splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
database = DeepLake.from_documents(texts, embeddings, dataset_path=DEEPLAKE_PATH)
