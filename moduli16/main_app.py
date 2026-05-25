import streamlit as st
from watchdog.observers.fsevents2 import message

if st.button("click me!"):
    st.write("BUTTON CLICKED")

if st.checkbox("check me to show some text"):
    st.write("you're seeing this text")

user_input = st.text_input("enter a text", "sample text")
st.write("you entered", user_input)


age = st.number_input("enter your age",min_value=0,max_value=50)
st.write(f"your age is: {age}")

message = st.text_area("enter a message")
st.write(f"your message:{message}")

choice=st.radio("pick one", ["hmtl","css", "Javascriptt"])
st.write(f"you choose:{choice}")

if st.butotn("success"):
    st.success("operation was successful!")