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

#US3/ BOOK CREATION
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, year):
        libro = {"titulo": titulo, "autor": autor, "year": year}
        self.libros.append(libro)
        print(f"Libro '{titulo}' agregado correctamente.\n")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.\n")
            return
        for i, libro in enumerate(self.libros, 1):
            print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['year']})")
        print()

    def actualizar_libro(self, indice, nuevo_titulo, nuevo_autor, nuevo_year):
        if 0 <= indice < len(self.libros):
            self.libros[indice] = {"titulo": nuevo_titulo, "autor": nuevo_autor, "year": nuevo_year}
            print("Libro actualizado correctamente.\n")
        else:
            print("Indice invalido.\n")

    def eliminar_libro(self, indice):
        if 0 <= indice < len(self.libros):
            libro_eliminado = self.libros.pop(indice)
            print(f"Libro '{libro_eliminado['titulo']}' eliminado correctamente.\n")
        else:
            print("Indice invalido.\n")