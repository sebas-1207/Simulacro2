# Juan Sebastian Lozano Siza. Grupo: R4
import json
import os

def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar...")

def leerDatos():
    try:
        with open('PaisCiudad.json', 'r', encoding="utf-8") as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        return {"Departamentos": []}     


def guardar_datos(datos):
    with open('PaisCiudad.json', 'w', encoding="utf-8") as file:
        json.dump(datos, file, indent=4)

def mostrarTodaslasCiudades(datos):
    print("{:^5} {:^15} {:^15} {:^12}".format("ID", "Nombre", "Imagen", "Coordenadas"))
    print("{:^5} {:^15} {:^15} {:^5} {:^5}".format("", "", "", "lat", "lon"))
    print("=" * 60)
    for departamento in datos["Departamentos"]:
        for ciudad in departamento["Ciudades"]:
            coordenados = ciudad["coordenadas"]
            print("{:^5} {:^15} {:^15} {:^5} {:^6}".format(ciudad["idCiudad"], ciudad["nomCiudad"], ciudad["imagen"], coordenados["lat"], coordenados["lon"]))

def crearCiudad(datos):
    os.system("cls")
    print("Los departamentos existentes son estos: ")
    print("{:^5} {:^15}".format("ID", "Nombre"))
    print("=" * 30)
    for departamento in datos["Departamentos"]:
        print("{:^5} {:^15}".format(departamento["idDep"], departamento["nomDepartamento"]))

    departamentoElegido = None
    while departamentoElegido is None:
        try:
            numeroDepartamento = int(input("Digite el ID del departamento: "))
            for departamento in datos["Departamentos"]:
                if departamento["idDep"] == numeroDepartamento:
                    departamentoElegido = departamento
                    break
            if departamentoElegido is None:
                print("¡Departamento no encontrado!")
        except ValueError:
            print("¡Ingrese un valor numérico válido!")

    if departamentoElegido:
        nombre = input("Digite el nombre de la ciudad: ")
        while not nombre:
            print("¡El nombre no puede estar vacío!")
            nombre = input("Digite el nombre de la ciudad: ")

        imagen = input("Digite la imagen de la ciudad(con .jpg al final): ")
        while not imagen:
            print("¡La imagen no puede estar vacía!")
            imagen = input("Digite la imagen de la ciudad(con .jpg al final): ")

        latitud = None
        while latitud is None:
            try:
                latitud = float(input("Digite la latitud de la ciudad: "))
            except ValueError:
                print("¡La latitud debe ser un valor numérico!")

        longitud = None
        while longitud is None:
            try:
                longitud = float(input("Digite la longitud de la ciudad: "))
            except ValueError:
                print("¡La longitud debe ser un valor numérico!")

        # Encuentra el máximo ID de ciudad actual
        max_id_ciudad = max(ciudad["idCiudad"] for depto in datos["Departamentos"] for ciudad in depto["Ciudades"])
        
        nueva_ciudad = {
            "idCiudad": max_id_ciudad + 1,
            "nomCiudad": nombre,
            "imagen": imagen,
            "coordenadas": {"lat": latitud, "lon": longitud}
        }

        departamentoElegido["Ciudades"].append(nueva_ciudad)
        guardar_datos(datos)

        os.system("cls")
        print("\n", "=" * 50)
        print("Ciudad agregada exitosamente".center(50))
        print("=" * 50)
    else:
        print("Departamento no encontrado.")


def eliminarCiudad(datos):
    os.system("cls")
    mostrarTodaslasCiudades(datos)
    ciudadElegida = None
    while ciudadElegida is None:
        try:
            numeroCiudad = int(input("Ingrese el ID de la ciudad a eliminar: "))
            for departamento in datos["Departamentos"]:
                ciudades = departamento["Ciudades"]
                ciudad_encontrada = None
                
                for ciudad in ciudades:
                    if ciudad["idCiudad"] == numeroCiudad:
                        ciudad_encontrada = ciudad
                        break
                
                if ciudad_encontrada:
                    ciudades.remove(ciudad_encontrada)
                    guardar_datos(datos)
                    os.system("cls")
                    print("\n", "=" * 50)
                    print("Ciudad eliminada exitosamente".center(50))
                    print("=" * 50)
                    ciudadElegida = True
                    break
            if ciudadElegida is None:
                print("Ciudad no encontrada")
        except ValueError:
            print("¡Ingrese un valor numérico válido!")

def crearDepartamento(datos):
    os.system("cls")
    nombre = input("Digite el nombre del departamento: ")
    while not nombre:
        print("¡El nombre no puede estar vacío!")
        nombre = input("Digite el nombre del departamento: ")

    nuevo_id = max(departamento["idDep"] for departamento in datos["Departamentos"]) + 1
    nuevo_departamento = {
        "idDep": nuevo_id,
        "nomDepartamento": nombre,
        "Ciudades": []
    }

    datos["Departamentos"].append(nuevo_departamento)
    guardar_datos(datos)

    os.system("cls")
    print("\n", "=" * 50)
    print("Departamento agregado exitosamente".center(50))
    print("=" * 50)


def eliminarDepartamento(datos):
    os.system("cls")
    mostrarTodoslosDepartamentos(datos)
    departamento_encontrado = None
    while departamento_encontrado is None:
        try:
            id_departamento = int(input("Digite el ID del departamento a eliminar: "))
            for departamento in datos["Departamentos"]:
                if departamento["idDep"] == id_departamento:
                    departamento_encontrado = departamento
                    break
            
            if departamento_encontrado:
                datos["Departamentos"].remove(departamento_encontrado)
                guardar_datos(datos)
                os.system("cls")
                print("\n", "=" * 50)
                print("Departamento eliminado exitosamente".center(50))
                print("=" * 50)
            else:
                print("Departamento no encontrado.")
        except ValueError:
            print("Digite un valor numérico válido")

def mostrarTodoslosDepartamentos(datos):
    print("{:^5} {:^15} {:^30}".format("ID", "Nombre", "Ciudades"))
    print("=" * 60)
    for departamento in datos["Departamentos"]:
        ciudades = ", ".join(ciudad["nomCiudad"] for ciudad in departamento["Ciudades"])
        print("{:^5} {:^15} {:^30}".format(departamento["idDep"], departamento["nomDepartamento"], ciudades))

def menu():
    while True:
        try:
            print("\n\n*** DEPARTAMENTOS-CIUDADES ***")
            print("\tMENU")
            print("1. Mostrar todas las ciudades")
            print("2. Crear ciudad")
            print("3. Eliminar ciudad")
            print("4. Crear departamento")
            print("5. Eliminar departamento")
            print("6. Mostrar todos los departamentos")
            print("7. Salir")
            op = int(input("\t>> Escoja una opción (1-7): "))
            if op < 1 or op > 7:
                msgError("Error. Opción Inválida (de 1 a 7).")
                continue
            return op
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 7).")
            continue

def main():
    os.system("cls")
    datos = leerDatos()
    while True:
        op = menu()
        if op == 1:
            os.system("cls")
            mostrarTodaslasCiudades(datos)
        elif op == 2:
            crearCiudad(datos)
        elif op == 3:
            eliminarCiudad(datos)
        elif op == 4:
            crearDepartamento(datos)
        elif op == 5:
            eliminarDepartamento(datos)
        elif op == 6:
            os.system("cls")
            mostrarTodoslosDepartamentos(datos)
        elif op == 7:
            salir = input("¿Está seguro que desea salir? (S/N): ")
            if salir.upper() == "S":
                print("\nGracias por usar el programa... Adiós...\n".center(80))
                break
            elif salir.upper() == "N":
                continue
            else:
                msgError("Error. Digite una opción válida.")
                continue

main()
