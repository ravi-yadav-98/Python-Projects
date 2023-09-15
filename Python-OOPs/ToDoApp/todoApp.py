
#Class for Task

class Task:
    def __init__(self, description, completed=False) -> None:
        self.description = description
        self.completed = completed
    
    def __str__(self) -> str:
        status = "Done" if self.completed else "Not Done"
        return f'{self.description} - {status}'


class ToDoList:

    def __init__(self) -> None:
        self.tasks = []
    
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):

        if 0<=index<len(self.tasks):
            del self.tasks[index]
    
    def mark_task_as_completed(self, index):
        if 0<=index<len(self.tasks):
            self.tasks[index].completed = True
    
    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f'{index}. {task}')


def main():

    todo_list = ToDoList()

    while True:
        print('\n ===To-Do-List ====')
        todo_list.display_tasks()

        print("\nOptions: ")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print('4. Quit')

        choice = input("Enter Your Choice(1/2/3/4)")

        if choice == "1":
            desc = input("Enter task Description: ")
            todo_list.add_task(desc)
        
        elif choice == "2":
            index = int(input("Enter Task index to remove: "))
            todo_list.remove_task(index)
        
        elif choice == "3":
            index = int(input("Enter Task index to remove: "))
            todo_list.mark_task_as_completed(index)
        elif choice =="4":
            print("Thanks for using ToDo app !!")
            print("Closing this app....")
            break
        else:
            print("Invalid Choice. Please choose a valid option..")

        
if __name__ == '__main__':
    main()