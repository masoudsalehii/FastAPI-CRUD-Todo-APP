from fastapi import FastAPI

app = FastAPI()

# This is a CRUD app: create, read, update, delete
# Get  --> Read Todo
# Post --> Create Todo
# Put --> Update Todo
# Delete --> Delete Todo


# minimal app - get request
@app.get("/", tags=['Root'])  # The category under which this get request will be classified
async def root() -> dict:
    return {"Ping": "Pong"}


# when someone insert the URL http://127.0.0.1:8000/todo, they will see the list of todos
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return {'data': todos}


# Add something with the post method
# the function get an input called todo which as an object in the form of dictionary
@app.post("/todo", tags =["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data":"A todo has been added!"
    }


# Update the current objects
@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] = body['Activity']
        return{
            "data": f"todo with id {id} has been updated"
        }
    return{
        "data": f"Todo with this id number {id} was not found!"
    }


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return{
                "data": f"Todo with the id {id} has been deleted"
            }
    return{"data":f"The todo with the id {id} was not found!"}



todos = [
    {"id": "1",
     "Activity": "Jogging for 2 hours at 7:00 AM."
     },
    {"id": "2",
     "Activity": "Writing my thesis at 2:00 PM."
    }
]


