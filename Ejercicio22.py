def usar_la_fuerza(mochila, indice=0, sable_de_luz_encontrado=False, objetos_sacados=0):
    """
    Función recursiva para buscar un sable de luz en una mochila.
    :param mochila: lista que representa los objetos en la mochila.
    :param indice: índice de la posición actual en la mochila.
    :param sable_de_luz_encontrado: variable booleana que indica si se ha encontrado el sable de luz.
    :param objetos_sacados: número de objetos sacados hasta el momento.
    :return: tupla que contiene la respuesta a los tres puntos del problema.
    """
    # Caso base: si ya se llegó al final de la mochila o se encontró el sable de luz, se detiene la búsqueda.
    if indice >= len(mochila) or sable_de_luz_encontrado:
        return sable_de_luz_encontrado, objetos_sacados
    
    # Se saca el objeto actual de la mochila.
    objeto_actual = mochila[indice]
    
    # Si se encuentra el sable de luz, se marca la variable correspondiente.
    if objeto_actual == "sable de luz":
        sable_de_luz_encontrado = True
    
    # Se sigue buscando recursivamente en la siguiente posición de la mochila.
    respuesta = usar_la_fuerza(mochila, indice + 1, sable_de_luz_encontrado, objetos_sacados + 1)
    
    # Se devuelve la respuesta.
    return respuesta[0], respuesta[1]


mochila = ["comida", "agua", "ropa", "sable de luz", "mapa"]
resultado = usar_la_fuerza(mochila)
print("Sable de luz encontrado:", resultado[0])
print("Objetos sacados:", resultado[1])
