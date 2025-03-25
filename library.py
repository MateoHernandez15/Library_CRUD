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