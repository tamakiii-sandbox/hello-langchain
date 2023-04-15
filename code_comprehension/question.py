import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

PROMPT = os.environ['PROMPT']
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
    PROMPT,
]
chat_history = []

for question in questions:
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result['answer']))
    print(f"-> **Question**: {question} \n")
    print(f"**Answer**: {result['answer']} \n")
