## Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula el promedio de las temperaturas por ciudad y semana.

    Parámetros:
    temperaturas (list): Una matriz tridimensional donde cada capa representa una ciudad,
                          cada fila una semana y cada columna un día de la semana.

    Retorna:
    dict: Un diccionario con los promedios de temperaturas por ciudad y semana.
    """
    num_ciudades = len(temperaturas)
    num_semanas = len(temperaturas[0])
    dias_semana = 7  # Cada semana tiene 7 días

    promedios = {}
    nombres_ciudades = ["Quito", "Ibarra", "García Moreno"]

    for ciudad in range(num_ciudades):
        promedios[ nombres_ciudades[ciudad] ] = []
        for semana in range(num_semanas):
            suma_temperaturas = sum(temperaturas[ciudad][semana])
            promedio_semana = suma_temperaturas / dias_semana
            promedios[ nombres_ciudades[ciudad] ].append(promedio_semana)
    
    return promedios

# Datos de temperaturas
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

# Calcular y mostrar los promedios
promedios = calcular_promedio_temperaturas(temperaturas)

for ciudad, promedios_semana in promedios.items():
    print(f"Promedio de temperaturas para {ciudad}:")
    for semana, promedio in enumerate(promedios_semana):
        print(f"  Semana {semana}: {promedio:.2f} grados Celsius")
    print()  # Separador entre ciudades


