import  streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.write("To boosts productivity.")
st.title("My To-Do App")
st.subheader("To do")
st.write("To boosts <b>productivity</b>", unsafe_allow_html=True)

st.text_input(label="Enter a to-do:", placeholder="Add a to-do",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

