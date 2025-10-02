from iu.menu_principal import menu_principal

def app():
    verdadero = True
    while verdadero:
        print(f"\nBienvenido a")
        menu_principal()
        print()
        opcion = input("Ingrese opción[0-4]: ")
        if opcion == '0':
            print("saliendo del sistema...")
            verdadero = False


app()