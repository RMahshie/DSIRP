# C++ program using a linked list to implement a to-do list application

## Introduction
This program is a simple C++ application that uses a linked list data structure to implement a to-do list application. It allows users to add new tasks to the list, print all the tasks in the list, and delete a task from the list.

## Linked List Data Structure
A linked list is a data structure that consists of a sequence of nodes, where each node contains a value and a pointer to the next node in the sequence. In this program, we use a linked list data structure to represent a to-do list, where each node in the list represents a task in the list.

## Program Structure
The program consists of three main parts: the Todo struct, the TodoList class, and the main function.

### The Todo Struct
The Todo struct defines the structure of each node in the linked list. It has two fields:
- task: a string representing the task description
- next: a pointer to the next node in the linked list

### The TodoList Class
The TodoList class is the main class of the program, which defines the methods to manipulate the linked list. It has the following methods:
- TodoList(): the constructor method, which initializes the head of the linked list to NULL
- addTask(string task): a method that adds a new task to the beginning of the linked list
- printTasks(): a method that prints all the tasks in the linked list
- deleteTask(string task): a method that removes a task from the linked list

### The main Function
The main function is the entry point of the program. It creates a new TodoList object called myList, adds three tasks to the list, prints all the tasks in the list, deletes the task "Buy groceries", prints the tasks again to confirm that the task was removed, and tries to delete the same task again to show the message "Task not found."

## Conclusion
This C++ program is a simple but practical example of how linked list data structures can be used in real-world applications. It demonstrates how a to-do list application can be implemented using a linked list data structure, which allows for efficient insertion, deletion, and traversal of the list.
