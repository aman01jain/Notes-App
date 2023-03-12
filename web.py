import streamlit as st
import functions


todos = functions.get_todos()

st.subheader("My Todo List")
st.write("This is to add your productivity")
st.title("My Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="New Todo..")