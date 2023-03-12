import streamlit as st
import functions


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todo(todos)



todos = functions.get_todos()

st.subheader("My Todo List")
st.write("This is to add your productivity")
st.title("My Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="New Todo..",
              on_change=add_todo, key='new_todo')
