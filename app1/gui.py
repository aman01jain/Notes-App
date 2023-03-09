import functions
import PySimpleGUI as sg

label = sg.Text("Enter a To-Do")
input_text = sg.InputText(tooltip="Enter a todo", key= "todo")
add_button = sg.Button("Add")

window = sg.Window('To-Do App',
                   layout=[[label], [input_text, add_button]],
                   font=("Helvetica", 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break
window.close()
