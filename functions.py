FILENAME = 'todo.txt'


def get_todos(filename=FILENAME):
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_Arg, filename=FILENAME):
    with open(filename, 'w') as file:
        file.writelines(todos_Arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
