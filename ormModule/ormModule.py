from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import models
from config import engine, SessionLocal

app1 = FastAPI()
db = SessionLocal()

class Emp(BaseModel):
    id: int
    name: str
    salary: int

@app1.get("/orm")
def get_all():
    get_all_emp = db.query(models.Employee).all()
    for emp in get_all_emp:
        if emp.id == 2:
            print(emp.name)
    me = db.query(models.Employee.name, models.Employee.salary)[0]
    print(me[0], me[1])
    return get_all_emp

@app1.post("/add_employee")
def add_employee(emp: Emp):
    new_emp1 = models.Employee(
        id = emp.id,
        name = emp.name,
        salary = emp.salary
    )
    
    db.add(new_emp1)
    db.commit()
     

