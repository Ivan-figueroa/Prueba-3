#ivan figueroa Diaz 

#Aqui inicio importando lo que usare a lo largo de mi programacion
import random
from statistics import geometric_mean

#Aqui inicio designando las bariables y juntandolas en una dupla

nombres = ["juan", "pedro", "maria", "marta", "ivan", 
           "anastacio", "juana", "pepe", "david", "manuel"]
saldos = [random.randint(500000, 1000000) for _ in range(10)]

clientes = list(zip(nombres, saldos))

#Aqui ire definiendo los diferentes saldos y sus promedios
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

saldos_bajos = [cliente for cliente in clientes if cliente[1] < 666667]
saldos_medios = [cliente for cliente in clientes if 666667 <= cliente[1] < 833334]
saldos_superiores = [cliente for cliente in clientes if cliente[1] >= 833334]