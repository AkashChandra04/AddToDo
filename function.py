FILEPATH = 'todo.txt'


def get_todo(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todo(todos_local, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_local)
