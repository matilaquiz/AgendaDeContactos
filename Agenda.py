import re


def mostrarOpciones():
    print("\n----- AGENDA DE CONTACTOS -----")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")
    resp = input("Elegi la opcion que desees ejecutar: ")
    try:
        return int(resp)
    except ValueError:
        print("Error, ingrese un numero del 1 al 5")
        return mostrarOpciones()


def agregarContacto(agenda):
    nombre = input("Ingresa el nombre y apellido del nuevo contacto: ").lower()
    # try:
    #   telefono=int(input("Ingresa el telefono del nuevo contacto"))
    # except ValueError:
    #    print("Error, ingrese un numero de telefono valido")
    #    return agregarContacto(agenda)
    while True:
        telefono = input("Ingresa el telefono del nuevo contacto: ")
        if telefono.isdigit() and 7 <= len(telefono) <= 15:
            telefono = int(telefono)
            break
        else:
            print("Error, ingrese un número de teléfono válido")
    while True:
        mail = input("Ingresa el mail del nuevo contacto: ")
        # Validar formato básico de email
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", mail):
            break
        else:
            print("Error, ingrese un mail válido")
    agenda[nombre] = {"telefono": telefono, "mail": mail}
    print(f"\n El contacto {nombre} agregado exitosamente.")


def buscarContacto(agenda):
    nombre = input("Escribe el nombre del contacto que buscas: ").lower()
    if nombre in agenda:
        print(f"\n Contacto encontrado: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['mail']}")
    else:
        print("\n Contacto no encontrado.")


def eliminarContacto(agenda):
    nombre = input("Escribe el nombre del contacto que deseas eliminar: ").lower()
    if nombre in agenda:
        agenda.pop(nombre)
        print(f"\n El contacto {nombre} se elimino correctamente")
    else:
        print(f"\n El contacto {nombre} no se encuentra en  esta agenda")


# def mostararTodosContactos(agenda):
def agendaContactos():
    agenda = {}
    while True:
        opcion = mostrarOpciones()
        if opcion == 1:
            agregarContacto(agenda)
        elif opcion == 2:
            buscarContacto(agenda)
        elif opcion == 3:
            eliminarContacto(agenda)
        elif opcion == 4:
            #           mostrarTodosContactos(agenda)
            pass
        elif opcion == 5:
            print("Estas saliendo de la aplicacion")
            break
        else:
            print("Error, ingrese un numero del 1 al 5")


agendaContactos()
