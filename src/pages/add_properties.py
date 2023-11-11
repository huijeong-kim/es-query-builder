import streamlit as st
import pandas as pd

st.set_page_config(page_title="Add mapping properties")

layouts = []

layout = st.text_area("mapping properties",
                      height=100,
                     label_visibility="visible",
                     disabled=False,
                     placeholder="field1: string, field2: text, ...")

# TODO use session state
if st.button("Add"):
    layouts.append(layout)
    layout=""
    
st.write(layouts)   
