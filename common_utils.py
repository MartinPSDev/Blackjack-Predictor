

   
# Cartas de los jugadores
cartas_jugadores = {}
global primera_carta_jugador 
global segunda_carta_jugador

def input_data(jugadores):
 global carta_descubierta_crupier
 carta_descubierta_crupier = tuple(input("Ingrese la primera carta del crupier en el siguiente formato [numero/letra, Palo]: ").split(', '))

 for i in range(1, jugadores + 1):
    primera_carta_jugador = tuple(input(f"Ingrese la primera carta del jugador {i} en el siguiente formato [numero/letra, Palo]: ").split(', '))
    segunda_carta_jugador = tuple(input(f"Ingrese la segunda carta del jugador {i} en el siguiente formato [numero/letra, Palo]: ").split(', '))
    cartas_jugadores[f"jugador_{i}"] = (primera_carta_jugador, segunda_carta_jugador)
 return cartas_jugadores
 

def crear_barajas(cantidad):
    palos = ['Corazones', 'Diamantes', 'Treboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [(valor, palo) for palo in palos for valor in valores]
    barajas_multiples = [((valor, palo), i + 1) for i in range(cantidad) for valor, palo in baraja]

    return barajas_multiples

def output_cartas():
# Mostrar cartas de los jugadores
 print("\nCartas de los jugadores:")
 for jugador, cartas in cartas_jugadores.items():
    print(f'{jugador}: {cartas[0]}, {cartas[1]}')

 print(f'\nCartas descubierta del crupier: {carta_descubierta_crupier}\n\n')

# Buscar las cartas para sacarlas del mazo
def buscar_cartas(cantidad):
    global nueva_baraja 
    nueva_baraja = crear_barajas(cantidad)

    cartas_a_buscar = [carta for cartas in cartas_jugadores.values() for carta in cartas] + [carta_descubierta_crupier]
    cartas_encontradas = []

    for carta in cartas_a_buscar:
        for carta_baraja in nueva_baraja:
            if carta_baraja[0] == carta:
                cartas_encontradas.append(carta_baraja)
                nueva_baraja.remove(carta_baraja)

    return cartas_encontradas



