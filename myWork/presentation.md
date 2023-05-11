# Our Linked To-Do List

## The Directive of our Code:

The purpose of the C++ program is to maintain a to-do list using a linked list data structure. The program allows the user to add and delete tasks, as well as display the current list of tasks. The linked list implementation allows for efficient adding and deleting of tasks, as well as easy traversal of the list for display purposes.

## How the Code Works:

The program maintains a linked list of Todo structs, where each struct represents a single task on the to-do list. The Todo struct contains a string member variable named task and a pointer to the next Todo struct in the list.

### Adding a Task:

The addTask function adds a new task to the beginning of the linked list. Here's how it works:


    void addTask(string task) {
        Todo* newTodo = new Todo;   // Allocate memory for a new Todo struct
        newTodo->task = task;       // Set the task string for the new Todo struct
        newTodo->next = head;       // Set the next pointer for the new Todo struct
        head = newTodo;             // Update the head pointer to point to the new Todo struct
    }


The function first allocates memory for a new Todo struct using the new operator. It then sets the task string and next pointer for the new Todo struct. Finally, it updates the head pointer to point to the new Todo struct, effectively adding the new task to the beginning of the list.

### Deleting a Task

The deleteTask function deletes a specified task from the linked list. Here's how it works:

    
    void deleteTask(string task) {
        Todo* current = head;   // Start at the head of the linked list
        Todo* previous = NULL;  // Keep track of the previous node
        while (current != NULL) {
            if (current->task == task) {  // If the current node matches the task to delete
            if (previous == NULL) {   // If the current node is the head of the list
                head = current->next; // Update the head pointer to point to the next node
            } else {
                previous->next = current->next;  // Update the previous node to skip the current node
            }
            delete current;  // Deallocate memory for the current node
            return;
        }
        previous = current;  // Move to the next node
        current = current->next;
    }
    cout << "Task not found." << endl;  // If task is not found
    }


The function first starts at the head of the linked list and moves through the list until it finds the Todo struct containing the specified task. Once it finds the correct Todo struct, it updates the next pointer for the previous Todo struct to <mark>skip</mark> the current Todo struct, <mark>effectively removing</mark> the current Todo struct from the linked list. It then <mark>deallocates</mark> the memory for the current Todo struct using the delete operator. If the specified task is not found, the function outputs an error message.

### Displaying the List

The displayList function simply traverses the linked list and outputs the task strings to the console. Here's how it works:


    void displayList() {
        Todo* current = head;  // Start at the head of the linked list
        while (current != NULL) {
            cout << current->task << endl;  // Output the task string
            current
