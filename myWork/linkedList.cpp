#include <iostream>
using namespace std;

struct Todo {
    string task;
    Todo* next;
};

class TodoList {
private:
    Todo* head;
public:
    TodoList() {
        head = NULL;
    }

    void addTask(string task) {
        Todo* newTask = new Todo;
        newTask->task = task;
        newTask->next = head;
        head = newTask;
    }

    void printTasks() {
        Todo* current = head;
        if (current == NULL) {
            cout << "No tasks in the list." << endl;
            return;
        }
        while (current != NULL) {
            cout << current->task << endl;
            current = current->next;
        }
    }
	void deleteTask(string task) {
    	Todo* current = head;
    	Todo* previous = NULL;
    	while (current != NULL) {
        	if (current->task == task) {
            	if (previous == NULL) {
                	head = current->next;
            	} else {
                	previous->next = current->next;
            	}
            	delete current;
            	current = NULL;
            	return;
        	}
        	previous = current;
        	current = current->next;
    	}
    	cout << "Task not found." << endl;
	}

};

int main() {
    TodoList myList;

    myList.addTask("Do laundry");
    myList.addTask("Buy groceries");
    myList.addTask("Clean room");

    myList.printTasks();

    myList.deleteTask("Buy groceries");

    myList.printTasks();

    myList.deleteTask("Buy groceries");

    return 0;
}
