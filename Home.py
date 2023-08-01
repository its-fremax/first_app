import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The best company".title())
st.write("This is an assignment given to improve our programming")

st.title("Our team")

df = pandas.read_csv("data.csv")

col1, col2, col3 = st.columns(3)

with col1:
    for index, rows in df[:4].iterrows():
        st.subheader(f"{rows['first name'].title()} {rows['last name'].title()}")
        st.write(rows["role"])
        st.image("images/" + rows["image"])

with col2:
    for index, rows in df[4:8].iterrows():
        st.subheader(f"{rows['first name'].title()} {rows['last name'].title()}")
        st.write(rows["role"])
        st.image("images/" + rows["image"])

with col3:
    for index, rows in df[8:].iterrows():
        st.subheader(f"{rows['first name'].title()} {rows['last name'].title()}")
        st.write(rows["role"])
        st.image("images/" + rows["image"])


