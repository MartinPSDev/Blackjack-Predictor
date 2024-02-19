from common_utils import*
import common_utils as cm

def sumar_valores_cartas(primera_carta_jugador,segunda_carta_jugador):
    # Asumiendo que primera_carta_jugador y segunda_carta_jugador están definidas y accesibles
    valor_primera_carta = int(primera_carta_jugador[0][0])  # Convierte el número de la primera carta a entero
    valor_segunda_carta = int(segunda_carta_jugador[0][0])  # Convierte el número de la segunda carta a entero
    
    suma = valor_primera_carta + valor_segunda_carta
    return suma

def estrategia_basica():
    if (cm.carta_descubierta_crupier == ('2', 'Corazones')) or (cm.carta_descubierta_crupier == ('2', 'Diamantes')) or \
          (cm.carta_descubierta_crupier  == ('2', 'Treboles'))or (cm.carta_descubierta_crupier == ('2', 'Picas') )and \
          (sumar_valores_cartas() > 4 and sumar_valores_cartas< 9 ):
        print ("\n\nPedir Carta")

    