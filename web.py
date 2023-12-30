import streamlit as st
import function


todos = function.get_todo()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    function.write_todo(todos)


st.title("To do App")

st.text_input('', placeholder='Add ToDo...', on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        function.write_todo(todos)
        del st.session_state[todo]
        st.rerun()




