import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


def load_tasks():
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass

    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    task_list = []
    for t_str in task_data:
        curr_t = {}
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False
        task_list.append(curr_t)

    return task_list


def save_tasks(task_list):
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


def display_task_details(task):
    disp_str = f"Task:             {task['title']}\n"
    disp_str += f"Assigned to:      {task['username']}\n"
    disp_str += f"Date Assigned:    {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date:         {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Task Description: {task['description']}\n"
    print(disp_str)


def display_tasks(task_list, filter_user=None):
    for i, t in enumerate(task_list, start=1):
        if not filter_user or t['username'] == filter_user:
            print(f"{i}.")
            display_task_details(t)


def register_user(username_password):
    new_username = input("New Username: ")
    if new_username in username_password.keys():
        print("Username already exists. Please choose a different username.")
        return

    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    if new_password == confirm_password:
        print("New user added")
        username_password[new_username] = new_password
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
    else:
        print("Passwords do not match")


def add_task(task_list, username_password):
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    save_tasks(task_list)
    print("Task successfully added.")


def view_mine(task_list, username):
    while True:
        display_tasks(task_list, username)
        choice = input("Enter the number of the task you want to select, or enter -1 to return to the main menu: ")
        if choice == "-1":
            break

        try:
            choice = int(choice)
            if 1 <= choice <= len(task_list):
                selected_task = task_list[choice - 1]
                edit_choice = input("Do you want to mark the task as complete (enter 'c') or edit the task (enter 'e')? ").lower()

                if edit_choice == 'c':
                    selected_task['completed'] = True
                    save_tasks(task_list)
                    print("Task marked as complete.")
                elif edit_choice == 'e' and not selected_task['completed']:
                    new_username = input("Enter the new username (press enter to keep the current username): ")
                    new_due_date_str = input("Enter the new due date (YYYY-MM-DD) (press enter to keep the current due date): ")

                    if new_username:
                        selected_task['username'] = new_username

                    if new_due_date_str:
                        try:
                            selected_task['due_date'] = datetime.strptime(new_due_date_str, DATETIME_STRING_FORMAT)
                        except ValueError:
                            print("Invalid datetime format. Task due date not updated.")

                    save_tasks(task_list)
                    print("Task updated successfully.")
                else:
                    print("Invalid choice. Please enter 'c' to mark as complete or 'e' to edit.")
            else:
                print("Invalid task number. Please choose a valid task.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            

def generate_reports(task_list, username_password):
    total_users = len(username_password)
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task['completed'])
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'].date() < date.today())

    with open("task_overview.txt", "w") as task_file:
        task_file.write(f"Task Overview\n")
        task_file.write(f"Total tasks: {total_tasks}\n")
        task_file.write(f"Completed tasks: {completed_tasks}\n")
        task_file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        task_file.write(f"Overdue tasks: {overdue_tasks}\n")
        task_file.write(f"Percentage of tasks incomplete: {(uncompleted_tasks / total_tasks) * 100:.2f}%\n")
        task_file.write(f"Percentage of tasks overdue: {(overdue_tasks / total_tasks) * 100}%\n")

    with open("user_overview.txt", "w") as user_file:
        user_file.write(f"User Overview\n")
        user_file.write(f"Total users: {total_users}\n")
        user_file.write(f"Total tasks: {total_tasks}\n")

        for username, password in username_password.items():
            user_tasks = [task for task in task_list if task['username'] == username]
            total_user_tasks = len(user_tasks)
            completed_user_tasks = sum(1 for task in user_tasks if task['completed'])
            uncompleted_user_tasks = total_user_tasks - completed_user_tasks
            overdue_user_tasks = sum(1 for task in user_tasks if not task['completed'] and task['due_date'].date() < date.today())

            user_file.write(f"\nUser: {username}\n")
            user_file.write(f"Total tasks assigned: {total_user_tasks}\n")
            user_file.write(f"Percentage of total tasks: {(total_user_tasks / total_tasks) * 100}%\n")
            user_file.write(f"Percentage of completed tasks: {(completed_user_tasks / total_user_tasks * 100) if total_user_tasks != 0 else 0:.2f}%\n")
            user_file.write(f"Percentage of uncompleted tasks: {(uncompleted_user_tasks / total_user_tasks * 100) if total_user_tasks != 0 else 0:.2f}%\n")
            user_file.write(f"Percentage of overdue tasks: {(overdue_user_tasks / total_user_tasks * 100) if total_user_tasks != 0 else 0:.2f}%\n")


def display_statistics(task_list, username_password):
    generate_reports(task_list, username_password)

    with open("task_overview.txt", "r") as task_file:
        task_overview = task_file.read()
        print(task_overview)

    with open("user_overview.txt", "r") as user_file:
        user_overview = user_file.read()
        print(user_overview)


def main():
    username_password = {}
    if os.path.exists("user.txt"):
        with open("user.txt", "r") as user_file:
            user_data = user_file.read().split("\n")

        for user in user_data:
            username, password = user.split(';')
            username_password[username] = password

    task_list = load_tasks()
    logged_in = False

    while not logged_in:
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")

        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True

    while True:
        print()
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

        if menu == 'r':
            register_user(username_password)
        elif menu == 'a':
            add_task(task_list, username_password)
        elif menu == 'va':
            display_tasks(task_list)
        elif menu == 'vm':
            view_mine(task_list, curr_user)
        elif menu == 'gr':
            generate_reports(task_list, username_password)
            print("Reports generated successfully.")
        elif menu == 'ds' and curr_user == 'admin':
            display_statistics(task_list, username_password)
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")


if __name__ == "__main__":
    main()
