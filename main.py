import  requests


url = "https://jsonplaceholder.typicode.com/todos"

#GET
get_response = requests.get(url)

if get_response.status_code == 200 :
    print(get_response.json())

#POST

to_do_item = {"userId": 2, "title" : "To do list", "completed": False}

post_url = "https://jsonplaceholder.typicode.com/todos"

#optional header
headers = {"Content Type" : "application/json"}
post_response = requests.post(url= post_url, data = to_do_item, headers= headers)
print(post_response.json())


#PUT
put_url = "https://jsonplaceholder.typicode.com/todos/15"
to_do_item_15 = {"userId": 2, "title": "put title", "completed": False}
put_response = requests.put(url= put_url, data= to_do_item_15)
print(put_response.json())

#PATCH
patch_url = "https://jsonplaceholder.typicode.com/todos/15"
to_do_item_patch_15 = {"title" : "Patch Test"}
patch_response = requests.patch(patch_url, data= to_do_item_patch_15)
print(patch_response.json())


#DELETE
patch_url = "https://jsonplaceholder.typicode.com/todos/15"
delete_response = requests.delete(patch_url)
print(delete_response.json())