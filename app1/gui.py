import functions
import PySimpleGUI as sg

label = sg.Text("Enter a To-Do")
input_text = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window('To-Do App', layout=[[label],[input_text, add_button]])
window.read()
window.close()
