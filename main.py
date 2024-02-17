from common_utils import *
import common_utils as cm
from B_Strategy import*

global cantidad, jugadores

cantidad = int(input("Ingrese la cantidad de mazos: "))
jugadores = int(input("Ingrese la cantidad de jugadores sin contar el crupier: "))



cm.input_data(jugadores)
cm.crear_barajas(cantidad)
cm.output_cartas()


sumar_valores_cartas(cartas_jugadores["jugador_1"][0], cartas_jugadores["jugador_1"][1])


def main ():
 what_to_do = estrategia_basica()
 print(f'Cartas encontradas: {cm.buscar_cartas(cantidad)}\n\n')
 print(f'Baraja Actual: {cm.nueva_baraja} \n\n')
 print(what_to_do)

if __name__ == "__main__":
    main()
