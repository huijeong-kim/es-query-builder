from dotenv import load_dotenv
import os
import streamlit as st

from simple_chatgpt_client import SimpleClient

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = SimpleClient(api_key)

st.title('ElasticSearch query builder')
st.divider()
    
layout = st.text_area("mapping properties",
                      height=100,
                     label_visibility="visible",
                     disabled=False,
                     placeholder="field1: string, field2: text, ...")

query = st.text_input("query you want in natural language:",
                      placeholder="search all docs whose field1 is \"movie\" sorted by field2")

result="No Result"

if st.button('build'):
    result = client.get(layout, query)    

st.write("")
st.write("")
st.write("")

st.code(result, language="json")
