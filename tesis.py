
import numpy as np


def calcular_porcentaje_ocupacion(capacidad_real, capacidad_instalada):
    porcentaje_ocupacion = (capacidad_real / capacidad_instalada) * 100
    return porcentaje_ocupacion


def colonia_hormigas(num_hormigas, capacidad_instalada, num_iteraciones, tasa_evaporacion, alfa, beta):
    # Crear matriz de feromonas
    num_capacidades = 100  # Número de capacidades posibles (de 1 a 100)
    feromonas = np.ones(num_capacidades)

    mejor_capacidad_real = 0
    mejor_porcentaje = 0

    for _ in range(num_iteraciones):
        for _ in range(num_hormigas):
            # Construir una solución candidata (una capacidad real) basada en las feromonas
            capacidad_real = np.random.choice(
                np.arange(1, num_capacidades + 1), p=feromonas/np.sum(feromonas))
            porcentaje_ocupacion = calcular_porcentaje_ocupacion(
                capacidad_real, capacidad_instalada)

            # Actualizar la mejor solución encontrada
            if porcentaje_ocupacion > mejor_porcentaje:
                mejor_capacidad_real = capacidad_real
                mejor_porcentaje = porcentaje_ocupacion

        # Actualizar feromonas
        feromonas = (1 - tasa_evaporacion) * feromonas
        feromonas[mejor_capacidad_real - 1] += alfa * mejor_porcentaje

    return mejor_capacidad_real, mejor_porcentaje


# Datos de entrada
capacidad_instalada = int(input("Ingrese la capacidad instalada (en horas): "))

# Ejecutar colonia de hormigas para obtener una mejor capacidad real y porcentaje de ocupación
num_hormigas = 10
num_iteraciones = 100
tasa_evaporacion = 0.1
alfa = 1.0
beta = 1.0

mejor_capacidad_real, mejor_porcentaje = colonia_hormigas(
    num_hormigas, capacidad_instalada, num_iteraciones, tasa_evaporacion, alfa, beta)

print(f"La mejor capacidad real encontrada es: {mejor_capacidad_real}")
print(
    f"El porcentaje de ocupación correspondiente es: {mejor_porcentaje:.2f}%")
