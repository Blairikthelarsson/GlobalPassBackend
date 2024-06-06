from fastapi import FastAPI , Depends
from sqlalchemy import  exc , create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
import uvicorn

app = FastAPI()
#

# Configuration de la base de données
SQLALCHEMY_DATABASE_URL = "sqlite:///xfield.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})
#Seesion HAndler
Session = sessionmaker(autocommit=False, autoflush=False,bind=engine)
#Call up for DataBase 


@app.get("/")
async def root():
 return {"message": "Hello World it's WORKS!!!"}




if __name__ == "__main__":
 uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)