import streamlit as st
import functions


todos = functions.get_todos()
st.title("My Todo App")
st.subheader("My Todo List")
st.write("This is to add your productivity")


for todo in todos:
    st.checkbox(todo)