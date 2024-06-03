model, prompt,parser

import openai

openai.api_key='key'

openai.ChatCompletion.create(model='',messages={'role':'user','content':'prompt'},temperature=0)


from langchain.prompts import ChatPromptTemplate
from langchain.chat_model import ChatOpenAI

temp=''
inp1,inp2=''

chat=ChatOpenAI(temp=0.0)

prompt_template=ChatPromptTemplate.from_template(temp)

template_format=prompt_template.format_messages(inp1=inp1,inp2=inp2)

chat(template_format)

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

temp=''

inp_schema=ResponseSchema(name='',description='')

schema=[inp_schema]

output=StructuredOutputParser.from_response_schemas(schema)

format=output.get_format_instructions()

prompt_template= ChatPromptTemplate.from_template(temp)

template_format=prompt_template.format_messages(text=inp1,format_instructions=format)

response=chat(template_format)

output.parse(response.content)


Memory

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from landchain.chat_model import ChatOpenAI


chat=ChatOpenAI(model='gpt-3.0-boost',temperature='0.0')

memory=ConversationBufferMemory()

convo=ConversationChain(llm=chat,memory=memory)

convo.predict(input='')

memory.buffer


memory.load_memory_variables({})

memory.save_context({'input':''},{'output':''})

from langchain.memory import ConversationBufferWindowMemory


memory=ConversationMemoryWindowBuffer(k=1)

convo=ConversationChain(llm=chat,memory=memory,temperature=0.0)

memory.buffer

convo.predict(input='')

memory.list_memory_variables({})

from langchain.memory import ConversationTokenBufferMemory


memory=ConversationTokenBufferMemory(llm=chat,max_token_limit=100)

convo=ConversationChain(llm=llm,memory=memory,temperature=0.0)


convo.predict(input='')

memory.buffer

memory.list_memory_variables({})


from langchain.chains import LLMChain

prompt_temp=ChatPromptTemplate.from_template(temp)

chain=LLMChain(llm=llm,prompt=prompt_temp)

chain.run(input)

from langchain import SimpleSequentialChain #one after another
from langchain.chains import SequentialChain

chain1=LLMChain(llm=llm,prompt=prompt1)
chain1.run(input)
chain2=LLMChain(llm=llm.prompt=prompt2)
chain2.run(input)

simplechain=SimpleSequentialChain(chains=[chain1,chain2])

simplechain.run(input)	



from langchain import MultiPromptChain
from langchain import PromptTemplate

from langchain.chains import LLMChain
prompt1={
template='',
input_variables=[]}
chain1=LLMChain(llm=chat,prompt=prompt1)

prompt2={template='',input_variables=['a']}


chain2=LLMChain(llm=chat,prompt=prompt2)

prompt3={template='',input_variables=['a','b']}

chain3=LLMChain(llm=chat,prompt=prompt3)


Multichain=MultiPromptChain(chains=[chain1,chain2,chain3],input_mapping={'a':'chain1','b':chain2})

multichain.run()


from langchain.chain import RetrievalQA
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from Ipython.display import display,Markdown
file='.csv'
loader=CSVLoader(filepath=file)

from langchain.indexes import VectorstoreIndexCreator

index=VectorstoresIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders([loader])

index.query(query='',llm=llm)

from langchain.embeddings import OpenAIEmbeddings

embeddings=OpenAIEmbeddings()

embed=embeddings.embed_query('')

doc=CSVLoader(filepath='')

db=DocArrayInMemorySearch.from_documents(doc,embeddings)

docs=db.similarity_search(query)

docs=''.join([i.page_content for i in docs])

response = llm.call_as_llm(f'{docs}question')

retriever=db.as_retriever()

stuff=RetriverQA.from_chain_type(chain_type='stuff',llm=llm,retriver=retriever)

response=stuff.run(query='')

display(Markdown(response))

response=index.query(query,llm)



there's Map reduce -> summarizes the output of each individual docs

refine -> summarizes the output of the documents sequential order doc-out->sum->doc-out->viceversa

Map_rerank -> returns a rank for the out which indicates the similarity score so we can choose the chuncks which we need more


from langchain.evaluation.qa import QAGenerativeChain


chain=QAGenaetativeChain(ChatOpenAI(model=''))

new=QAGenerativeChain.apply_and_parse([{'doc':i} for i in docs[:5]])

import langchain 
langchain.debug = True

from langchain.chain.evaltion.qa import evaluate

from langchain.evaluation.qa import QAEvalChain

eval=QAEvalChain.from_llm(llm=chat)

graded_outputs= eval.evaluate(examples,predictions)

for i, eg in enumerate(examples):
    print(f"Example {i}:")
    print("Question: " + predictions[i]['query'])
    print("Real Answer: " + predictions[i]['answer'])
    print("Predicted Answer: " + predictions[i]['result'])
    print("Predicted Grade: " + graded_outputs[i]['text'])
    print()


from langchain.agents import load_tools,initialize_agent,AgentType
