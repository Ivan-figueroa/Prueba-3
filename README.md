import random
import statistics

nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Laura", "Miguel", "Lucía"]

salarios = [random.randint(500000, 1000000) for _ in range(len(nombres))]

def afp(salario):
    afp = 0.12
    return salario * (1 - salario)

def salud(salario):
    salud = 0.07
    return salario * (1 - salario)

def liquido(salario):
    liquido = 0.19
    return salario * (1 - salario)

def mostrar_menu():
    print("----- Menú -----")
    print("1. Ver saldos ")
    print("2. Ver saldos más bajos, altos y medios")
    print("3. Ver promedio de sueldos")
    print("4. Ver media geométrica de sueldos")
    print("5. Salir")


def saldos_bajos_altos_medios(salarios):
    salarios_ordenados = sorted(salarios)
    minimo = salarios_ordenados[0]
    maximo = salarios_ordenados[-1]
    medio = salarios_ordenados[len(salarios_ordenados) // 2]
    return minimo, maximo, medio


def media_geometrica(salarios):
    if len(salarios) == 0:
        return None
    producto = 1
    for salario in salarios:
        producto *= salario
    return producto ** (1 / len(salarios))


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            print("Clasificar sueldos:")
            for i in range(len(nombres)):
                nombre = nombres[i]
                salario = salarios[i]
                print(f"nombre empleado salario")
                print(f"{nombre}:      ${salario}")
            input("Presione Enter para continuar...")
        
        elif opcion == "2":
            print("Saldos con descuento aplicado afp (12%):")
            for i in range(len(nombres)):
                nombre = nombres[i]
                print(f" Nombre    Salario     Ds salud  Ds afp  Liquido")
                print(f"{nombre}: {salario}  {salud}    {afp}   {liquido}")
            input("Presione Enter para continuar...")
        
        elif opcion == "3":
            minimo, maximo, medio = saldos_bajos_altos_medios(salarios)
            print(f"Saldos más bajos, altos y medios:")
            print(f"Saldos más bajos: ${minimo}")
            print(f"Saldos más altos: ${maximo}")
            print(f"Saldo medio: ${medio}")
            input("Presione Enter para continuar...")
            
        elif opcion == "4":
            media_geom = media_geometrica(salarios)
            if media_geom:
                print(f"Media geométrica de sueldos: ${media_geom:.2f}")
            else:
                print("No se puede calcular la media geométrica de una lista vacía.")
            input("Presione Enter para continuar...")
        
        elif opcion == "5":
            print("Saliendo del programa...")
            print("Desarrollado por Ivan Figueroa")
            print("RUT: 21.733.391-1")
            
if __name__ == "__main__":
    main()
print(f"Media geometrica del salod:{saldo_media_geometrica(clientes)}")
    
