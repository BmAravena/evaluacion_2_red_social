def app():
    verdadero = True
    while verdadero:
        opcion = input("Ingrese opción[0-4]: ")
        if opcion == '0':
            print("saliendo del sistema...")
            verdadero = False


app()