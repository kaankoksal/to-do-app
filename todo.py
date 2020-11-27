import sys

def usage_info():   
    usage_text = "\nCommand Line Todo Application \n============================= \n\nCommand line arguments: \n    -l    Lists all tasks \n    -a    Adds new task \n    -r    Removes a task \n    -c    Completes a task" 
    print(usage_text)

def list():
    print("Here are your tasks:")
    with open('tasks.txt', 'r') as f:
        print(f.read())
        f.close

def no_task_given():
    print("Unable to add: Task not provided")

def add():
    task = sys.argv[2]
    with open('tasks.txt', 'a') as f:
        f.write(task + "\n")
        f.close
    print("Added " + task + " to the task list")

def remove():
    with open('tasks.txt', 'r') as f:
        lines = f.readlines()
    with open('tasks.txt', 'w') as f:
        for line in lines:
            if line.strip("\n") != sys.argv[2]:
                f.write(line)
                f.close
            print(str(sys.argv[2]) + " removed from tasks!")

def complete():
    with open('tasks.txt', 'r') as f:
        lines = f.readlines()
    with open('tasks.txt', 'w') as f:
        for line in lines:
            if line.strip("\n") != sys.argv[2]:
                f.write(line)
                f.close
            print(str(sys.argv[2]) + " completed. Great job!")

def unknown():
    print('\nYou have entered an unknown command.\nPlease refer to the usage information below')
    usage_info()

def too_many():
    print('\nYou have entered too many arguments.\n(" ") Please make sure you type your task in brackets (" ")')

def no_file():
    print('Unable to find tasks.txt, please make the file available')

def cant_remove():
    print('Unable to remove: task not provided')

def cant_complete():
    print('Unable to complete: task not provided')

print(sys.argv)

if len(sys.argv) == 1:
        usage_info()
elif len(sys.argv) == 2 and sys.argv[1] == "-l":
    with open('tasks.txt', 'r') as f:
        tasks = f.read()
    if tasks == "":
        print("No tasks for today!")
    else:
        list()
elif len(sys.argv) == 2 and sys.argv[1] == "-a":
    no_task_given()
elif len(sys.argv) == 3 and sys.argv[1] == "-a":
    try:
        add()
    except FileNotFoundError:
        no_file()
elif len(sys.argv) == 2 and sys.argv[1] == "-r":
    cant_remove()
elif len(sys.argv) == 3 and sys.argv[1] == "-r":
    try:
        remove()
    except FileNotFoundError:
        no_file()
elif len(sys.argv) == 2 and sys.argv[1] == "-c":
    cant_complete()
elif len(sys.argv) == 3 and sys.argv[1] == "-c":
    try:
        complete()
    except FileNotFoundError:
        no_file()
elif len(sys.argv) == 2:
    unknown()
elif len(sys.argv) == 3:
    unknown()
elif len(sys.argv) > 3:
    too_many()
    usage_info()
