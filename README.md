# Prueba-3
#ivan figueroa Diaz 

#Aqui inicio importando lo que usare a lo largo de mi programacion
import random,csv
from statistics import geometric_mean

#Aqui inicio designando las bariables y juntandolas en una dupla
nombres = ["juan", "pedro", "maria", "marta", "ivan", 
           "anastacio", "juana", "pepe", "david", "manuel"]
saldos = [random.randint(500000, 1000000) for _ in range(10)]

clientes = list(zip(nombres, saldos))
