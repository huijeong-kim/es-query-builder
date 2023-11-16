from dotenv import load_dotenv
import os
import streamlit as st
import json

from simple_chatgpt_client import SimpleClient
from chatgpt_assistant_client import AssistantClient

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = SimpleClient(api_key)

st.title('ElasticSearch query builder')

if 'layouts' not in st.session_state:
    st.session_state['layouts'] = []
    
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

tab1, tab2 = st.tabs(["fields", "build"])

with tab1:
    user_input = st.text_area("mapping properties",
                     height=500,
                     label_visibility="visible",
                     disabled=False,
                     placeholder="field1: string, field2: text, ...",
                     key='user_input')

    c1, c2 = st.columns([1, 10])
    if c1.button('Add'):
        if user_input and user_input not in st.session_state['layouts']:
            #st.session_state['user_input'] = ""
        
            try:
                json_data = json.loads(user_input)
                compacted = json.dumps(json_data, indent=2)
                
                st.session_state['layouts'].append(compacted)
            except json.JSONDecodeError:
                st.warning("Invalid JSON input")
                            
    if c2.button('Clear'):
        user_input = "" # TODO it's not working
    
    st.divider()
    st.write("Fields list. click right button to remove")
    
    for index, element in enumerate(st.session_state['layouts']):
        b1, b2, b3 = st.columns([1, 10, 1])
        b1.write(f'{index}')
        b2.code(element, language="json")
        if b3.button(f"rm{index}"):
            st.session_state['layouts'].remove(element)

with tab2:
    st.write('Select fields you want to use')
    layout = st.selectbox(
        '',
        st.session_state['layouts']
    )
    st.code(layout, language="json")
    
    st.write("")
    st.write("")
    
    st.write("Query you want in natural language")
    query = st.text_input("Search all docs whose...",
                        placeholder="field1 is \"movie\" sorted by field2")

    result="No Result"
        
    if st.button('build'):
        with st.spinner("Running..."):
            result = client.get(layout, query)    

    st.write("")
    st.write("")
    st.write("")

    st.write("Result:")
    st.code(result, language="json")
