import itertools
import string
import time


# Función para generar contraseñas
def generate_passwords(charset, length):
    """
    Genera todas las posibles combinaciones de contraseñas de una longitud específica
    utilizando un conjunto de caracteres dado.

    Args:
        charset (str): Conjunto de caracteres a usar para generar contraseñas.
        length (int): Longitud de las contraseñas a generar.

    Yields:
        str: Contraseña generada.
    """
    for password in itertools.product(charset, repeat=length):
        yield "".join(password)


# Función para intentar adivinar la contraseña
def try_passwords(charset, password_to_find):
    """
    Realiza un ataque de fuerza bruta para encontrar una contraseña específica.

    Args:
        charset (str): Conjunto de caracteres a usar para generar contraseñas.
        password_to_find (str): La contraseña que se desea encontrar.

    Returns:
        tuple: (contraseña encontrada, número de intentos, tiempo transcurrido)
    """
    start_time = time.time()
    attempts = 0
    for password in generate_passwords(charset, len(password_to_find)):
        attempts += 1
        print(f"Intento {attempts}: {password}")
        if password == password_to_find:
            end_time = time.time()
            return password, attempts, end_time - start_time
    return None, attempts, time.time() - start_time


# Función para evaluar la seguridad de una contraseña
def evaluate_password_security(password):
    """
    Evalúa la seguridad de una contraseña en función de la cantidad de caracteres únicos.

    Args:
        password (str): La contraseña a evaluar.

    Returns:
        int: Nivel de seguridad de la contraseña (1 a 5).
    """
    unique_chars = len(set(password))
    if unique_chars == 1:
        return 1
    elif unique_chars == 2:
        return 2
    elif unique_chars == 3:
        return 3
    elif unique_chars == 4:
        return 4
    else:
        return 5


# Función principal
def main():
    """
    Función principal que ejecuta el programa.
    Solicita al usuario una contraseña de 4 caracteres alfanuméricos y realiza un ataque de fuerza bruta
    para encontrarla, luego evalúa su seguridad.
    """
    name = input("Por favor, ingresa tu nombre: ")
    while True:
        password = input(
            "Por favor, ingresa una contraseña de 4 caracteres alfanuméricos: "
        )
        if (
            all(c in string.ascii_letters + string.digits for c in password)
            and len(password) == 4
        ):
            break
        else:
            print(
                "La contraseña debe contener exactamente 4 caracteres alfanuméricos. Inténtalo de nuevo."
            )

    charset = string.ascii_letters + string.digits

    print(f"Realizando ataque de fuerza bruta para la contraseña de {name}...")
    found_password, attempts, duration = try_passwords(charset, password)

    if found_password:
        print(f"\n¡Contraseña encontrada: {found_password}!")
        print(f"Intentos: {attempts}")
        print(f"Tiempo transcurrido: {duration:.2f} segundos")

        security_rating = evaluate_password_security(password)
        print(f"Seguridad de la contraseña (1-5): {security_rating}")
    else:
        print("\nNo se pudo encontrar la contraseña.")


# Ejecución del programa
if __name__ == "__main__":
    main()
