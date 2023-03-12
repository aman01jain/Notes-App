from functions import get_todos,write_todo
import time
now = time.strftime("%d %b, %Y %H:%M:%S")
print("it is",now)
while True:
    user_action = input("type add,show,edit,remove or exit :")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todo(todos)

    elif user_action.startswith("show"):
        todos = get_todos('todo.txt')
        for i, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{i+1}-{item}"
            print(row)
    elif user_action.startswith("remove"):
        try:
            num = int(user_action[7:])
            index = num-1
            todos = get_todos()
            removed_todo = todos[index].strip('\n')
            todos.pop(num-1)
            write_todo(todos)
            message = f" todo {removed_todo} was removed from the list "
            print(message)
        except IndexError:
            print("There is no item with that no.")
            continue
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_item = input("enter the new todo: ")
            todos[number] = new_item + '\n'
            write_todo(todos)
        except ValueError:
            print("Your command is invalid")
            continue
    elif user_action.startswith("exit"):
        break
    else :
        print("Command is inncorect")
print("bye!!")