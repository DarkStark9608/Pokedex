Crear contenedor docker

En carpeta docker
    docker build -t mi_project1:v1 . 
En carpeta code
    docker volume create webapp
    docker volume ls
    docker volume inspect webapp
    docker container run -d -it -v "$PWD":/home/code --net=host --name project_1 -h oscarrdz --mount source=webapp,target=/app mi_project1:v1

Correr docker
    docker start -i project_1

Crear Base de datos
    sqlite3 bd.sqlite < bd.sql 






extras:
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]" 

pip install pyjwt==v1.7.1



















@app.post("/usuarios", response_model=Respuesta)
async def post_usuarios(usuario:User ,credentials: HTTPAuthorizationCredentials=Depends(securityBearer)):
    with sqlite3.connect(DATABASE_URL) as connection:
        password_b = hashlib.md5(usuario.password.encode())
        password = password_b.hexdigest()        
        cursor = connection.cursor()
            
        cursor.execute(
                "INSERT INTO usuarios (username, password, level, token) VALUES (? , ? , ? , ?)",
                (usuario.username, usuario.password, usuario.level, usuario.token))
            
        user = cursor.fetchone()
        if not user:
            raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Basic"},
                )
    return user[0] #ADMIN  







    from datetime import datetime
import jwt
key = 'david@mail.com'+str(datetime.now())
message = { 'yek': key }
secret = 'dndnVvODY4Yzc2bdnVvODY4Yzc2bzhz'
token_bytes = jwt.encode(message, secret, algorithm='HS256')
token = token_bytes.decode()



print(token)



