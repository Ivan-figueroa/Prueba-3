# Prueba-3
#ivan figueroa Diaz 

#Aqui inicio importando lo que usare a lo largo de mi programacion
import random,csv
from statistics import geometric_mean

#Aqui inicio designando las bariables y juntandolas en una dupla
nombres = ["juan", "pedro", "maria", "marta", "ivan", 
           "anastacio", "juana", "pepe", "david", "manuel"]
saldos = [random.randint(500000, 1000000) for _ in range(10)]

#Aqui ire definiendo los diferentes saldos y sus promedios
clientes = list(zip(nombres, saldos))
def saldo_mas_alto(clientes):
    max_saldo = clientes[0]
    for cliente in clientes:
        if cliente[1] > max_saldo[1]:
            max_saldo = cliente
    return max_saldo


def saldo_mas_bajo(clientes):
    min_saldo = clientes[0]
    for cliente in clientes:
        if cliente[1] < min_saldo[1]:
            min_saldo = cliente
    return min_saldo


def saldo_promedio(clientes):
    total_saldo = sum(cliente[1] for cliente in clientes)
    return total_saldo / len(clientes)

def saldo_media_geometrica(clientes):
    saldo = [cliente[1]for cliente in clientes]
    return geometric_mean(saldos)

saldos_bajos = [cliente for cliente in clientes if cliente[1] < 500000]
saldos_medios = [cliente for cliente in clientes if 500000 <= cliente[1] < 800000]
saldos_superiores = [cliente for cliente in clientes if cliente[1] >= 800000]

#Aqui almaceno los datos en un repositorio tipo csv 
with open ("Repositorio.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["nombres","saldos"])
    writer.writerows(clientes)

#Y por ultimo queda imprimir los resultados    
print(f"Clientes y sus saldos: {clientes}")
print(f"Saldos bajos: {saldos_bajos}")
print(f"Saldos medios: {saldos_medios}")
print(f"Saldos superiores: {saldos_superiores}")
print(f"Saldo más alto:{saldo_mas_alto(clientes)}")
print(f"Saldo más bajo:{saldo_mas_bajo(clientes)}")
print(f"Saldo promedio:{saldo_promedio(clientes)}")
print(f"Media geometrica del salod:{saldo_media_geometrica(clientes)}")
    
