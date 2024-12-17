# Usuario y contraseña predeterminados
default_username = "admin"
default_password = "admin123"

# Lista para almacenar los usuarios registrados
registered_users = []

# Registrar el usuario predeterminado
registered_users.append({"username": default_username, "password": default_password})

print("Registro de Usuario")

# Bucle principal para registrar usuarios
while True:
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    # Verificar si el usuario ya existe
    if username in [user['username'] for user in registered_users]:
        print("El nombre de usuario ya existe. Por favor, elija otro.")
    else:
        # Agregar usuario a la lista de usuarios registrados
        registered_users.append({"username": username, "password": password})
        print(f"Usuario {username} registrado exitosamente.")

    show_more = input("¿Desea registrar otro usuario? (s/n): ")
    if show_more.lower() != 's':
        break

# Mostrar todos los usuarios registrados al final
print("Usuarios Registrados:")
for user in registered_users:
    print(f"Usuario: {user['username']}")