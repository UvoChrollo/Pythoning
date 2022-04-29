# import package
from fastapi import FastAPI

# defining as app
app = FastAPI()

# get route
@app.get('/')

# what is this route do ?
def index():
    return "Hello World !"