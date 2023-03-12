import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w")as file:
        pass

sg.theme("BlueMono")

clock = sg.Text(key='clock')
label = sg.Text("Enter a To-Do")
input_text = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")
exit_button = sg.Button('Exit')

window = sg.Window('To-Do App',
                   layout=[[clock],
                           [label],
                           [input_text, add_button],
                           [list_box, edit_button, remove_button],
                           [exit_button]],
                   font=("Helvetica", 14))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value= time.strftime("%d %b, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todos = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todos
                functions.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("no Item in the list present", font=("Helvetica", 14))
        case 'Remove':
            try:
                todo_to_remove = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todo(todos)
                window['todos'].update(values =todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("No Item in the list present", font=("Helvetica", 14))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
