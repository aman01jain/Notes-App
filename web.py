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

for index,todo in enumerate(todos):
    checkbox =st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="", placeholder="New Todo..",
              on_change=add_todo, key='new_todo')
