from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

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
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Provide proper elastic search query with provided fields. Do not explain, just a query"
            },
            {
                "role": "user",
                "content": f"with the doc fields {layout}, {query}"
            }
        ],
        model="gpt-3.5-turbo"
    )
    
    result = completion.choices[0].message.content
    

st.write("")
st.write("")
st.write("")

st.code(result, language="json")

