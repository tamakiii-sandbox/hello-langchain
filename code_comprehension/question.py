import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

OPENAI_MODEL = 'gpt-4'# 'gpt-3.5-turbo',
DEEPLAKE_PATH = os.environ['DEEPLAKE_API_KEY']

embeddings = OpenAIEmbeddings()
database = DeepLake(dataset_path=DEEPLAKE_PATH, read_only=True, embedding_function=embeddings)

retriever = database.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['fetch_k'] = 100
retriever.search_kwargs['maximal_marginal_relevance'] = True
retriever.search_kwargs['k'] = 20

def filter(x):
    # filter based on source code
    if 'com.google' in x['text'].data()['value']:
        return False

    # filter based on path e.g. extension
    metadata =  x['metadata'].data()['value']
    return 'scala' in metadata['source'] or 'py' in metadata['source']

### turn on below for custom filtering
# retriever.search_kwargs['filter'] = filter

model = ChatOpenAI(model=OPENAI_MODEL)
qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)

questions = [
    "What does favCountParams do?",
    "is it Likes + Bookmarks, or not clear from the code?",
    "What are the major negative modifiers that lower your linear ranking parameters?",
    "How do you get assigned to SimClusters?",
    "What is needed to migrate from one SimClusters to another SimClusters?",
    "How much do I get boosted within my cluster?",
    "How does Heavy ranker work. what are it’s main inputs?",
    "How can one influence Heavy ranker?",
    "why threads and long tweets do so well on the platform?",
    "Are thread and long tweet creators building a following that reacts to only threads?",
    "Do you need to follow different strategies to get most followers vs to get most likes and bookmarks per tweet?",
    "Content meta data and how it impacts virality (e.g. ALT in images).",
    "What are some unexpected fingerprints for spam factors?",
    "Is there any difference between company verified checkmarks and blue verified individual checkmarks?",
]
chat_history = []

for question in questions:
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result['answer']))
    print(f"-> **Question**: {question} \n")
    print(f"**Answer**: {result['answer']} \n")