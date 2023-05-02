def usar_la_fuerza(mochila, indice=0, sable_de_luz_encontrado=False, objetos_sacados=0):
    

    if indice >= len(mochila) or sable_de_luz_encontrado:
        return sable_de_luz_encontrado, objetos_sacados
    
    objeto_actual = mochila[indice]
    
    if objeto_actual == "sable de luz":
        sable_de_luz_encontrado = True
    
   
    respuesta = usar_la_fuerza(mochila, indice + 1, sable_de_luz_encontrado, objetos_sacados + 1)
    
  
    return respuesta[0], respuesta[1]


mochila = ["comida", "agua", "ropa", "sable de luz", "mapa"]
resultado = usar_la_fuerza(mochila)
print("Sable de luz encontrado:", resultado[0])
print("Objetos sacados:", resultado[1])
