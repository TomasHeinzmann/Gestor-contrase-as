from basededatos import *
def validarEntre(min, max, inp):
    try:
        x = int(inp)
        while x < min or x > max:
            print(f"Error, el valor ingresado no está dentro del rango [{min}, {max}]")
            x = int(input(f"Ingrese un valor entre {min} y {max}: "))
        return x
    except ValueError:
        print("Error, el valor ingresado no es un número válido")
        return None

def menu():
    print("******** GESTOR DE CONTRASEÑAS ********")
    print("- Bienvenido - Ingrese una opción")
    print("1) Ver todas las contraseñas")
    print("2) Agregar contraseña")
    print("3) Borrar contraseña")
    print("4) Ver contraseña por cuenta")
    print("0) Salir")
    return validarEntre(0, 4, input("Ingrese una opción: "))

def principal():
    opc = menu()
    while opc != 0:
        if opc == 1:
            verTodasContrasena()
        elif opc == 2:
            con = input("Ingrese nueva contraseña: ")
            usu = input("Ingrese cuenta asociada: ")
            nuevaContrasena(con, usu)
        elif opc == 3:
            borrarContrasena()
        elif opc == 4:
            buscar = input("Ingrese cuenta a buscar: ")
            buscarContrasena(buscar)
        opc = menu()
    print("Gracias por usar el programa!")

if __name__ == "__main__":
    principal()
