

cantidad = int(input("Ingrese la cantidad de mazos: "))
jugadores = int(input("Ingrese la cantidad de jugadores sin contar el crupier: "))


def crear_barajas(cantidad):
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [(valor, palo) for palo in palos for valor in valores]
    barajas_multiples = [((valor, palo), i+1) for i in range(cantidad) for valor, palo in baraja ]

    return barajas_multiples

nueva_baraja= crear_barajas(cantidad)

print (nueva_baraja)


