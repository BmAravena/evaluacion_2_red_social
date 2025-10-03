from iu.menu_principal import menu_principal

def app():
    verdadero = True
    while verdadero:
        print(f"\nBienvenido a")
        menu_principal()    
        print()
        opcion = input("Ingrese opción[0-7]: ")
        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
        elif opcion == '6':
            pass
        elif opcion == '7':
            pass
        elif opcion == '0':
            print("saliendo del sistema...")
            verdadero = False


app()