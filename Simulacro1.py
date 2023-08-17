# Juan Sebastian Lozano Siza. Grupo: R4
import json
import os

def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar ...")

def mostrarMascotas():
    os.system("clear")
    with open("PetShopping.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print("{:^5} {:^15} {:^20} {:^10} {:^10} {:^30}".format("", "Tipo", "Raza", "Talla", "Precio", "Servicios"))
        print("="*96)
        for idx, pet in enumerate(data["pets"], start=1):
            servicios = ', '.join(pet['servicios'])
            print("{:^5} {:^15} {:^20} {:^10} {:^10} {:^30}".format(idx, pet['tipo'], pet['raza'], pet['talla'], pet['precio'], servicios))

def crearMascota():
    os.system("clear")
    tipo = input("Ingrese el tipo de mascota: ")
    while not tipo:
        msgError("¡El tipo no puede estar vacío!")
        tipo = input("Ingrese el tipo de mascota: ")

    raza = input("Ingrese la raza de la mascota: ")
    while not raza:
        msgError("¡La raza no puede estar vacía!")
        raza = input("Ingrese la raza de la mascota: ")

    talla = input("Ingrese la talla de la mascota: ")
    while not talla:
        msgError("¡La talla no puede estar vacía!")
        talla = input("Ingrese la talla de la mascota: ")

    precio = None
    while precio is None:
        try:
            precio = int(input("Ingrese el precio de la mascota: "))
        except ValueError:
            msgError("¡El precio debe ser un número válido!")

    servicios = input("Ingrese los servicios de la mascota (separados por comas): ").split(',')
    while not any(servicios):
        msgError("¡Debes ingresar al menos un servicio!")
        servicios = input("Ingrese los servicios de la mascota (separados por comas): ").split(',')

    nueva_mascota = {
        "tipo": tipo,
        "raza": raza,
        "talla": talla,
        "precio": precio,
        "servicios": [s.strip() for s in servicios]
    }

    os.system("clear")

    print("\n", "=" * 50)
    print("Mascota agregada correctamente".center(50))
    print("=" * 50)
    
    with open("PetShopping.json", "r") as file:
        data = json.load(file)

    data["pets"].append(nueva_mascota)

    with open("PetShopping.json", "w") as file:
        json.dump(data, file, indent=4)

def mostrarMascotaPorTipo():
    os.system("clear")
    while True:
        encontrado=False
        tipo_elegido = input("Ingrese el tipo de mascota a mostrar: ")
        with open("PetShopping.json", "r") as file:
            data = json.load(file)
            print("{:^15} {:^20} {:^10} {:^10} {:^30}".format("Tipo", "Raza", "Talla", "Precio", "Servicios"))
            print("="*96)
            for pet in data["pets"]:
                if pet["tipo"].lower() == tipo_elegido.lower():
                    encontrado=True
                    servicios = ', '.join(pet['servicios'])
                    print("{:^15} {:^20} {:^10} {:^10} {:^30}".format(pet['tipo'], pet['raza'], pet['talla'], pet['precio'], servicios))
            if not encontrado:
                print("\n","=" * 30)
                print("La mascota no existe".center(30))
                print("=" * 30)
            else:
                break              

def actualizarMascota():
    os.system("clear")
    with open("PetShopping.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
    tipos_mascotas = [pet['tipo'] for pet in data["pets"]]
    while True:
        mostrarMascotas()
        tipo_elegido = input("Ingrese el tipo de mascota a actualizar: ")
        while not tipo_elegido:
            msgError("Debes elegir un tipo de mascota")
            tipo_elegido = input("Ingrese el tipo de mascota a actualizar: ")

        if tipo_elegido in tipos_mascotas:
            for pet in data["pets"]:
                if pet["tipo"] == tipo_elegido:
                    print("Datos actuales:")
                    print("{:^15} {:^20} {:^10} {:^10} {:^30}".format("Tipo", "Raza", "Talla", "Precio", "Servicios"))
                    print("="*96)
                    servicios = ', '.join(pet['servicios'])
                    print("{:^15} {:^20} {:^10} {:^10} {:^30}".format(pet['tipo'], pet['raza'], pet['talla'], pet['precio'], servicios))
                    
                    pet["tipo"] = input("Ingrese el nuevo tipo de mascota: ")
                    while not pet["tipo"]:
                        msgError("¡El tipo no puede estar vacío!")
                        pet["tipo"] = input("Ingrese el nuevo tipo de mascota: ")

                    pet["raza"] = input("Ingrese la nueva raza de la mascota: ")
                    while not pet["raza"]:
                        msgError("¡La raza no puede estar vacía!")
                        pet["raza"] = input("Ingrese la nueva raza de la mascota: ")

                    pet["talla"] = input("Ingrese la nueva talla de la mascota: ") 
                    while not pet["talla"]:
                        msgError("¡La talla no puede estar vacía!")
                        pet["talla"] = input("Ingrese la nueva talla de la mascota: ")   

                    pet["precio"] = None
                    while pet["precio"] is None:
                        try:
                            pet["precio"] = int(input("Ingrese el nuevo precio de la mascota: "))
                        except ValueError:
                            msgError("El precio debe ser un número válido")        

                    pet["servicios"] = input("Ingrese los nuevos servicios de la mascota (separados por comas): ").split(',')
                    while not any(pet["servicios"]):
                        msgError("¡Debes ingresar al menos un servicio!")
                        pet["servicios"] = input("Ingrese los nuevos servicios de la mascota (separados por comas): ").split(',')

            with open("PetShopping.json", "w") as file:
                json.dump(data, file, indent=4)
            
            os.system("clear")
            print("\n", "=" * 50)
            print("Mascota actualizada correctamente".center(50))
            print("=" * 50)
            break
        else:
            print("Tipo de mascota no encontrado. Intente nuevamente")

def eliminarMascota():
    with open("PetShopping.json", "r") as file:
        data = json.load(file)
        
    tipos_mascotas = [pet['tipo'] for pet in data["pets"]]
    mostrarMascotas()
    while True:
        tipo_elegido = input("Ingrese el tipo de mascota que desea eliminar: ")
        if tipo_elegido in tipos_mascotas:
            data["pets"] = [pet for pet in data["pets"] if pet["tipo"] != tipo_elegido]
            with open("PetShopping.json", "w") as file:
                json.dump(data, file, indent=4)  
            os.system("clear")
            print("\n", "=" * 50)
            print("Mascota eliminada correctamente".center(50))
            print("=" * 50)
            break
        else:
            print("Tipo de mascota no encontrado. Intente nuevamente.")


def menu():
    while True:
        try:
            print("\n\n*** PET SHOPPING ***")
            print("\tMENU")
            print("1. Mostrar todas las mascotas")
            print("2. Crear nueva mascota")
            print("3. Mostrar mascota por tipo")
            print("4. Modificar mascota")
            print("5. Eliminar mascota")
            print("6. Salir")
            op = int(input("\t>> Escoja una opción (1-6): "))
            if op < 1 or op > 6:
                msgError("Error. Opción Inválida (de 1 a 6).")
                continue
            return op
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 6).")
            continue

def main():
    while True:
        op = menu()
        if op == 1:
            mostrarMascotas()
        elif op == 2:
            crearMascota()
        elif op == 3:
            mostrarMascotaPorTipo()
        elif op == 4:
            actualizarMascota()
        elif op == 5:
            eliminarMascota()
        elif op == 6:
            salir = input("¿Está seguro que desea salir? (S/N): ")
            if salir.upper() == "S":
                print("\nGracias por usar el programa... Adiós...\n".center(80))
                break
            elif salir.upper() == "N":
                continue
            else:
                msgError("Error. Digite una opción válida.")
                continue

# Programa Principal
main()
