from fastapi import FastAPI

app = FastAPI()

# minimal app - get request
@app.get("/", tags=['ROOT'])
def root() -> dict:
    return{"Ping": "Pong"}


# Get - Read ToDo Item
@app.get("/todo", tags=['todos'])
def get_todo() -> dict:
    return{"data": todos}

# Post - Create ToDo Item
@app.post("/todo", tags=['todos'])
def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been added!"
    }

# Put - Update ToDo Item
@app.put("/todo/{id}", tags=['todos'])
def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] = body['Activity']
            return {
                "data":f"Todo with id {id} has been updated"
            }
    return {
        "data":f"Todo with id {id} was not found"
    }

# Delete - Delete ToDo Item
@app.delete("/todo/{id}", tags=["todos"])
def delete_todo(id:int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return {
                "data":f"Todo with id {id} has been deleted"
            }
    return {
        "data":f"Todo with id {id} wasn't found"
    }


todos = [
    {"id": "1",
    "Activity": "Put the bins out at 7pm"
    },
    {
    "id": "2",
    "Activity": "Bring the bins in at 7am"
    }
]