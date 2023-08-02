import streamlit as st
from send_email import send_email

with open("topics.csv", "r") as file:
    content = file.readlines()[1:]

with st.form("Email form"):
    user_email = st.text_input("Your email Address")
    list_content = [items.strip("\n") for items in content]
    topic = st.selectbox("What topic do you want  to discuss?", list_content)

    raw_message = st.text_area("Text")
    message = f"""\
Subject: New message from {user_email}

Topic: {topic}
{raw_message}
"""

    submit = st.form_submit_button("Submit")
    if submit:
        if topic:
            send_email(message)
    st.info("Your message was sent successfully.")


