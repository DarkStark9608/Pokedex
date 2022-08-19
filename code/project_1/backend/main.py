from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import hashlib  # importa la libreria hashlib 
import sqlite3 
import os
from secrets import token_bytes
from base64 import b64encode

app = FastAPI()
DATABASE_URL = os.path.join("sql/bd.sqlite")
security = HTTPBasic() 
securityBearer= HTTPBearer()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://0.0.0.0:8080",
    "*",               
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):   
    username: str
    password: str
    level: int
    token: str

class Usuario(BaseModel):
    email: str
    password: str

class Respuesta (BaseModel) :  
    message: str  

def get_current_level(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    with sqlite3.connect(DATABASE_URL) as connection:
        cursor = connection.cursor()      
        cursor.execute(
            "SELECT token FROM usuarios WHERE token = ? ;",
            (credentials.credentials,))       
        user = cursor.fetchone()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or passworddddddddddddddddddddd",
                headers={"WWW-Authenticate": "Bearer"},
            )
    return user[0] #ADMIN


@app.get("/", response_model=Respuesta) 
async def index(): 
    return {"message": "API POKEDEX"} 

@app.post("/login", status_code=status.HTTP_202_ACCEPTED,
summary="login",description="Inicio de sesion")
async def post_clientes(cliente: Usuario):
    with sqlite3.connect(DATABASE_URL) as connection:
        password_b = hashlib.md5(cliente.password.encode())
        password = password_b.hexdigest()        
        cursor = connection.cursor()
        
        cursor.execute(
            "SELECT token FROM usuarios WHERE username = ? and password = ?",
            (cliente.email, password),)
        
        user = cursor.fetchone()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    return user[0] #ADMIN    
    

@app.get("/pokemon", response_model=Respuesta)
async def list(credentials: HTTPAuthorizationCredentials=Depends(securityBearer)):
    return {"message": "API POKEDEX"} 

@app.post("/usuarios", response_model=Respuesta)
async def post_usuarios(usuario:User ,token:str=Depends(get_current_level)):
    with sqlite3.connect(DATABASE_URL) as connection:
        password_b = hashlib.md5(usuario.password.encode())
        password = password_b.hexdigest()        
        cursor = connection.cursor()
            
        cursor.execute(
                "INSERT INTO usuarios (username, password, level, token) VALUES (? , ? , ? , ?)",
                (usuario.username, usuario.password, usuario.level, usuario.token,),)            
        user = connection.commit()
        
        if user:
            return {"message": "Cliente no agregado"}
        else:
            return {"message":"Cliente agregado"}
    