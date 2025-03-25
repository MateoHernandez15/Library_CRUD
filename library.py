# US1/ CREATE REGISTER
users = {}
def createUser(): 
    id = input("Ingrese su documento: ")
    if id in users:
        print("Este documento ya está registrado. Intente iniciar sesion.\n")
        return
    user_name = input("Ingrese su nombre: ")
    user_last_name = input("Ingrese su apellido: ")
    phone = input("Ingrese su numero de telefono: ")
    user_email = input("Ingrese su correo electronico: ")
    user_password = input("Ingrese su contraseña: ")
    users[id] = {
        "nombre": user_name,
        "apellido": user_last_name,
        "telefono": phone,
        "email": user_email,
        "contraseña": user_password
    }
    print(f"Usuario {user_name} registrado correctamente.\n")   

#US2/ LOGIN AND VERIFICATION TO PASSWORD
def login():
    id = input("Ingrese su documento: ")
    if id not in users:
        print("Este usuario no esta registrado. Por favor, cree una cuenta.\n")
        return None
    password = input("Ingrese su contraseña: ")
    if users[id]["contraseña"] == password:
        print(f"Bienvenido {users[id]['nombre']}!\n")
        return id
    else:
        print("Contraseña incorrecta.\n")
        return None
def showUsers():
    if not users:
        print("No hay usuarios registrados.\n")
        return
    for id, user in users.items():
        print(f"Documento: {id}, Nombre: {user['nombre']} {user['apellido']}, Teléfono: {user['telefono']}, Email: {user['email']}")
    print()