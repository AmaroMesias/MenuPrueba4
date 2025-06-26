
usuario = {}


while True:
    print("1- Ingresar usuario ")
    print("2- Buscar usuario ")
    print("3- Eliminar usuario ")
    print("4- Salir")
    
    opcion = input("Ingrese opcion: ")

    
    if opcion == "1":
        nombre = input("Ingrese nombre de usuario: ")
        if nombre in usuario:
            print("El usuario ya existe, ingrese otro.")
            continue

        sexo = input("Ingrese sexo (M o F):")
        if sexo.upper() != "M" and sexo.upper() != "F":
            print("Debe ingresar M o F solamente.")
            continue

        cont = input("Ingrese contraseña: ")

        if len(cont) < 8:
            print("Contraseña muy corta. Debe tener al menos 8 caracteres.")
            continue
        if " " in cont:
            print("La contraseña no debe tener espacios.")
            continue
        tltra = False
        tnum = False
        for c in cont:
            if c.isalpha():
                tltra = True
            if c.isdigit():
                tnum = True
        if not tltra or not tnum:
            print("La contraseña debe tener al menos una letra y un numero.")
            continue

        print("Contraseña valida.")
        usuario[nombre] = {"sexo": sexo.upper(), "contrasena": cont}
        print("Usuario correctamente ingresado")
    
    elif opcion == "2":
        buscar = input("Ingrese usuario a buscar: ")
        if buscar in usuario:
            print("El sexo del usuario es:", usuario[buscar]["sexo"], 
                  "y la contraseña es:", usuario[buscar]["contrasena"])
        else:
            print("Usuario no encontrado")

    
    elif opcion == "3":
        eliminar = input("Ingrese el nombre de usuario que quiere eliminar: ")
        if eliminar in usuario:
            del usuario[eliminar]
            print("Usuario eliminado")
        else:
            print("No se pudo eliminar usuario")

    elif opcion == "4":
        print("Salio del programa")
        break

    else:
        print("Debe seleccionar una opcion valida")