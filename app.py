import streamlit as st

from llama_index import SimpleDirectoryReader
from llama_index import ServiceContext
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex
from dotenv import  load_dotenv
import os
import openai
load_dotenv()
os.environ['OPENAI_API_KEY']= "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"
#openai.api_key=os.getenv("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")





with st.sidebar:
    st.title("Chatbot con informacion propia")
    st.markdown('''
    ## About 
    This App es implementada con las siguientes tecnologias:
    - [streamlit](https://streamlit.io) 
    - [Llama Index](https://gpt-index.readdocs.io)
    - [OpenAI](https://platform.openai.com/doc/models) LLM Model
                
                ''')

def main():
    st.header("Chatbot con informacion propia")
    reader = SimpleDirectoryReader(input_dir='./data', recursive = True)
    docs = reader.load_data()
    service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo",temperature=0.5, system_prompt ="eres una machine learning y tu objetivo es responder preguntas"))
    index = VectorStoreIndex.from_documents(docs, service_context=service_context)
    #print(index)
    query= st.text_input("responde preguntas relacionadas con la informacion")

    if query:

       chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose = True)
       response = chat_engine.chat(query)
       st.write(response.response)



    
if __name__=='__main__':

    main()
