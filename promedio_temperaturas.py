# Crear una matriz tridimensional para almacenar las temperaturas
# Supongamos que tenemos 3 ciudades (Quito, Ibarra, García Moreno), 7 días de la semana y 4 semanas

# Inicializar la matriz de temperaturas
temperaturas = [
    # Quito
    [
        # Semana 0
        [18, 19, 18, 20, 21, 22, 19],
        # Semana 1
        [19, 20, 21, 22, 21, 20, 19],
        # Semana 2
        [20, 21, 22, 23, 22, 21, 20],
        # Semana 3
        [21, 22, 23, 24, 23, 22, 21]
    ],
    # Ibarra
    [
        # Semana 0
        [16, 17, 16, 18, 19, 18, 17],
        # Semana 1
        [17, 18, 19, 20, 19, 18, 17],
        # Semana 2
        [18, 19, 20, 21, 20, 19, 18],
        # Semana 3
        [19, 20, 21, 22, 21, 20, 19]
    ],
    # García Moreno
    [
        # Semana 0
        [14, 15, 14, 16, 17, 16, 15],
        # Semana 1
        [15, 16, 17, 18, 17, 16, 15],
        # Semana 2
        [16, 17, 18, 19, 18, 17, 16],
        # Semana 3
        [17, 18, 19, 20, 19, 18, 17]
    ]
]

# Calcular el promedio de temperaturas por ciudad y semana
num_ciudades = len(temperaturas)
num_semanas = len(temperaturas[0])  # Suponemos que todas las ciudades tienen el mismo número de semanas
dias_semana = 7  # Suponemos que cada semana tiene 7 días

# Nombres de las ciudades
nombres_ciudades = ["Quito", "Ibarra", "García Moreno"]

for ciudad in range(num_ciudades):
    print(f"Promedio de temperaturas para {nombres_ciudades[ciudad]}:")
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(dias_semana):
            suma_temperaturas += temperaturas[ciudad][semana][dia]
        promedio_semana = suma_temperaturas / dias_semana
        print(f"  Semana {semana}: {promedio_semana:.2f} grados Celsius")
    print()  # Separador entre ciudades

