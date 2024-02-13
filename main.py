import common_utils as cm
from B_Strategy import*

global cantidad, jugadores

cantidad = int(input("Ingrese la cantidad de mazos: "))
jugadores = int(input("Ingrese la cantidad de jugadores sin contar el crupier: "))



cm.input_data(jugadores)
cm.crear_barajas(cantidad)
cm.output_cartas()
cm.buscar_cartas(cantidad)
sumar_valores_cartas(cm.primera_carta_jugador,cm.segunda_carta_jugador)


def main ():
 what_to_do = estrategia_basica()
 print(f'Cartas encontradas: {cm.buscar_cartas()}\n\n')
 print(f'Baraja Actual: {cm.nueva_baraja} \n\n')
 print(what_to_do)

if __name__ == "__main__":
    main()
