import requests

base_url = "https://jsonplaceholder.typicode.com/todos"

# Task 1: Get the 200 most recent TODOs
response = requests.get(f"{base_url}?_limit=200")
if response.status_code == 200:
    todos = response.json()
    print("Task 1: Get the 200 most recent TODOs")
    for todo in todos:
        print(f"ID: {todo['id']}, Title: {todo['title']}")
else:
    print(f"Failed to get TODOs. Status code: {response.status_code}")

# Task 2: Create a TODO 
# I wasn't sure if the list needed to be printed out again after creating and deleted but I included them also
new_todo_title = input("\nEnter the title for the new TODO: ")
new_todo_completion = input("\nEnter the completion status for the new TODO: ")
new_todo_userId = input("\nEnter the user Id for the new TODO: ")

new_todo = {
    "title": new_todo_title,
    "completed": new_todo_completion,
    "userId": new_todo_userId
}

response = requests.post(base_url, json=new_todo)
if response.status_code == 201:
    created_todo = response.json()
    print("\nTask 2: Create a TODO")
    print(f"Created TODO with ID: {created_todo['id']}, Title: {created_todo['title']}")
    
    # List TODOs after creating a new one
    response = requests.get(f"{base_url}?_limit=200")
    if response.status_code == 200:
        todos = response.json()
        print("\nList of TODOs after creating a new one:")
        for todo in todos:
            print(f"ID: {todo['id']}, Title: {todo['title']}")
    else:
        print(f"Failed to get TODOs. Status code: {response.status_code}")
else:
    print(f"Failed to create TODO. Status code: {response.status_code}")

# Task 3: Delete a TODO by ID
todo_id_to_delete = input("\nEnter the ID of the TODO you want to delete: ")

delete_url = f"{base_url}/{todo_id_to_delete}"

response = requests.delete(delete_url)
if response.status_code == 200:
    print(f"\nTask 3: Delete a TODO with ID {todo_id_to_delete}")
    print(f"TODO with ID {todo_id_to_delete} deleted successfully.")
    
    # List TODOs after deleting one
    response = requests.get(f"{base_url}?_limit=200")
    if response.status_code == 200:
        todos = response.json()
        print("\nList of TODOs after deleting one:")
        for todo in todos:
            print(f"ID: {todo['id']}, Title: {todo['title']}")
    else:
        print(f"Failed to get TODOs. Status code: {response.status_code}")
else:
    print(f"Failed to delete TODO. Status code: {response.status_code}")
