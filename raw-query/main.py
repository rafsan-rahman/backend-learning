from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

@app.get("/")
def home():
    return {"data":"yet to come"}

# db_name = "apitest"
# db_user = "postgres"
# db_pswd = "aust_cse_40"
# db_host = "127.0.0.1"
# db_port = "5432"

# conn = psycopg2.connect(
#     dbname = db_name,
#     user = db_user,
#     password = db_pswd,
#     host = db_host,
#     port = db_port
    
# )

# class Employee(BaseModel):
    id: int
    name: str
    salary: int

# @app.get("/{name}")
# def employee_information(name: str):
#     cursor = conn.cursor()
#     select_query = "SELECT * FROM employee WHERE name = %s"
#     cursor.execute(select_query, (name,))
    
#     employee = cursor.fetchone()
    
#     cursor.close()
#     if employee:
#         return employee
#     else:
#         return {"ERROR": "Data does not exist"}

# class Post(BaseModel):
#     id:int
#     name:str
#     age:int
#     salary:Optional[float] = None
    
# my_post = [{'id':1, 'name':'hasad', 'age':29, 'salary':90000.00},
#            {'id':2, 'name':'orshed', 'age':29, 'salary':30000.00}]

# @app.get('/index')
# def root():
#     return {'message': 'welcome to fastapi universe'}

# @app.post('/createpost')
# def create_post(data: dict = Body(...)):
#     return {"text": data['text'],"content": data['content']}

# @app.post('/updatepost')
# def update_post(post: Post):
#     post = post.dict()
#     my_post.append(post)
#     return {'data': my_post}