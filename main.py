

cantidad = int(input("Ingrese la cantidad de mazos: "))
jugadores = int(input("Ingrese la cantidad de jugadores sin contar el crupier: "))
primera_carta_jugador = tuple(input("Ingrese una de sus cartas en el siguiente formato [numero/letra, Palo]: ").split(', '))
segunda_carta_jugador = tuple(input("Ingrese su otra carta en el siguiente formato [numero/letra, Palo]: ").split(', '))
primera_carta_crupier = tuple(input("Ingrese una de las cartas del crupier en el siguiente formato [numero/letra, Palo]: ").split(', '))
segunda_carta_crupier = tuple(input("Ingrese su otra carta en el siguiente formato [numero/letra, Palo]: ").split(', '))



def crear_barajas(cantidad):
    palos = ['Corazones', 'Diamantes', 'Treboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [(valor, palo) for palo in palos for valor in valores]
    barajas_multiples = [((valor, palo), i+1) for i in range(cantidad) for valor, palo in baraja ]

    return barajas_multiples

nueva_baraja= crear_barajas(cantidad)

#print (nueva_baraja)
print(f'jugadores: {jugadores}\n\n sus cartas: {primera_carta_jugador}\t{segunda_carta_jugador}\n\n cartas del crupier:{primera_carta_crupier}\t{segunda_carta_crupier}\n\n')
 

#Buscar las cartas para sacarlas del mazo

def buscar_cartas():
    global nueva_baraja
    cartas_a_buscar = [primera_carta_jugador, segunda_carta_jugador, primera_carta_crupier, segunda_carta_crupier]
    cartas_encontradas = []

    for carta in cartas_a_buscar:
        for carta_baraja in nueva_baraja:
            if carta_baraja[0] == carta:
                cartas_encontradas.append(carta_baraja)
                nueva_baraja.remove(carta_baraja)
            
    return cartas_encontradas

print(f'Cartas encontradas: {buscar_cartas()}\n\n')  
print(f'Baraja Actual: {nueva_baraja} \n\n')

      

