from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

user = 'postgres'
password = 'aust_cse_40'
host = '127.0.0.1'
port = '5432'
db_name = 'apitest'

def get_connection():
    return create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, db_name))

try:
    engine = get_connection()
    print(f"connection for {host}, user: {user} created sucessfully")
except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()