password_liuva = 123456
email_liuva = "liuvasalas01@gmail.com"
afirmacion = "si"

inicio_sesion = input("¿Deseas iniciar sesion como usuario? Responde si/no: ").lower()

if inicio_sesion == afirmacion:
    email = input("Ingresa tu email: ").lower()
    password = int(input("Ingresa tu contraseña: "))
    if email == email_liuva and password == password_liuva:
        print("email y contraseña correctos")
    else:
        print("email o contraseña son incorrectos")
else:
    print("no esta iniciando sesion como usuario")

informacion = input("¿Necesitas mas información? Responde si/no: ").lower()

if informacion == afirmacion and inicio_sesion == afirmacion:
    if email != email_liuva:
        print("el email ingresado es incorrecto")
    elif password != password_liuva:
        print("El correo ingresado es correcto pero no la contraseña")
    else:
        print("todo lo ingresado esta correcto")
else:
    print("fin del programa")
