import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetching user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data["name"]

        # Fetching TODO list data
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Counting the number of completed tasks
        completed_tasks = [task for task in todo_data if task["completed"]]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todo_data)

        # Formatting and printing the output
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)
    except KeyError:
        print("Error: Invalid Employee ID.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
