# TODO APP

Todo App is a basic command line application. It can be used to store your daily tasks with functionalities like listing the tasks, adding new tasks and removing or completing a task.

## Installation

Cloning this repository to your local system is sufficient for the installation.

## Dependencies 

In order to use any of the commands that the application has to offer, the 'tasks.txt' file must be accessible, preferably in the same directory as 'todo.py' file.

In order for the application to run, the terminal window must be opened in '.../to-do-app' directory in your local system.

When giving commands to the application, the first argument must always be " python todo.py " as this is not an executable file.
Please note that " python todo.py " alone will print out the usage information.
-----> example : python todo.py -l # lists all tasks

## Usage 

In the terminal window, 
$ cd .../to-do-app

python todo.py # prints out usage information

python todo.py -l # lists all tasks 
                  # if there are no tasks to be displayed
                  # it will print 'No tasks for today!'
                  # in case another argument after '-l' are given, app will inform the user that it is an unknown argument and will ask the user to refer to the usage information
                  # in case multiple arguments after '-l' are given, app will inform the user that they entered too many arguments and will ask the user to refer to the usage information

python todo.py -a '' # adds mew task (task should be given inside the brackets)
                     # after using the command correcyl, app will print "Added 'task' to the task list'
                     # if the user neglects to use brackets when entering the task, app will inform the user that they entered too many arguments and will mention that tasks should be provided inside brackets. No task will be added in this case.
                     # in case no argument is given after '-a' app will print 'Unable to add: task not provided'
                     # in case tasks.txt is not found, app should print the file not found message

python todo.py -r '' # removes the task which should be specified inside the brackets
                     # in case no argument is provided after '-r', app will print 'Unable to remove: no task given'
                     # in case command is given correctly, app will remove the specified task from the file and will print 'task' removed from task list!

python todo.py -c '' # completes the tasks which was provided inside the brackets 
                     # in case no argument is given after '-c', app will print 'Unable to complete: no task given' 
                     # in case command is given correctly, it will remove the specified task from the file and will print 'task' completed!

## Highlighted Features

$ list() 
    # First, prints "Here are your tasks:"
    # Goes to a new line, and opens tasks.txt in read mode as 'f'
    # prints the lines in the file with f.read()
    # closes the file 

$ add() 
    # takes the third command line argument and stores it in 'task'
    # opens tasks.txt in append mode as 'f'
    # appends the task to the end of the file and then goes to a new line
    # closes the file 
    # prints "added 'task' to the task list"

$ remove()
    # opens tasks.txt in read mode as f
    # reads the lines in the file and stores them in 'lines'
    # opens tasks.txt in write mode as f
    # writes 'lines' into tasks.txt excluding the third command line argument
    # closes the file
    # prints "'task' removed from task list"

$ complete()
    # opens tasks.txt in read mode as f
    # reads the lines in the file and stores them in 'lines'
    # opens tasks.txt in write mode as f
    # writes 'lines' into tasks.txt excluding the third command line argument
    # closes the file
    # prints "'task' completed. Great job!"


