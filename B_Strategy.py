from .common_utils import*
import common_utils as cm

def sumar_valores_cartas(primera_carta_jugador,segunda_carta_jugador):
    # Asumiendo que primera_carta_jugador y segunda_carta_jugador están definidas y accesibles
    valor_primera_carta = int(primera_carta_jugador[0][0])  # Convierte el número de la primera carta a entero
    valor_segunda_carta = int(segunda_carta_jugador[0][0])  # Convierte el número de la segunda carta a entero
    
    suma = valor_primera_carta + valor_segunda_carta
    return suma

def estrategia_basica():
    if (cm.carta_descubierta_crupier == ('2', 'Corazones')) or (cm.carta_descubierta_crupier == ('2', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('2', 'Treboles'))  or (cm.carta_descubierta_crupier == ('2', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('3', 'Corazones')) or (cm.carta_descubierta_crupier == ('3', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('3', 'Treboles'))  or (cm.carta_descubierta_crupier == ('3', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('4', 'Corazones')) or (cm.carta_descubierta_crupier == ('4', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('4', 'Treboles'))  or (cm.carta_descubierta_crupier == ('4', 'Picas') )or\
       (cm.carta_descubierta_crupier == ('5', 'Corazones')) or (cm.carta_descubierta_crupier == ('5', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('5', 'Treboles'))  or (cm.carta_descubierta_crupier == ('5', 'Picas') )or\
       (cm.carta_descubierta_crupier == ('6', 'Corazones')) or (cm.carta_descubierta_crupier == ('6', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('6', 'Treboles'))  or (cm.carta_descubierta_crupier == ('6', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('7', 'Corazones')) or (cm.carta_descubierta_crupier == ('7', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('7', 'Treboles'))  or (cm.carta_descubierta_crupier == ('7', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('8', 'Corazones')) or (cm.carta_descubierta_crupier == ('8', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('8', 'Treboles'))  or (cm.carta_descubierta_crupier == ('8', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('9', 'Corazones')) or (cm.carta_descubierta_crupier == ('9', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('9', 'Treboles'))  or (cm.carta_descubierta_crupier == ('9', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('A', 'Corazones')) or (cm.carta_descubierta_crupier == ('A', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('A', 'Treboles'))  or (cm.carta_descubierta_crupier == ('A', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('K', 'Corazones')) or (cm.carta_descubierta_crupier == ('K', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('K', 'Treboles'))  or (cm.carta_descubierta_crupier == ('K', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('J', 'Corazones')) or (cm.carta_descubierta_crupier == ('J', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('J', 'Treboles'))  or (cm.carta_descubierta_crupier == ('J', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('Q', 'Corazones')) or (cm.carta_descubierta_crupier == ('Q', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('Q', 'Treboles'))  or (cm.carta_descubierta_crupier == ('Q', 'Picas') ) \
        and  ((sumar_valores_cartas(cartas_jugadores["jugador_1"][0], cartas_jugadores["jugador_1"][1]) > 4) and \
              (sumar_valores_cartas(cartas_jugadores["jugador_1"][0], cartas_jugadores["jugador_1"][1])< 9) ):
     print ("\n\nPedir Carta")

    elif (sumar_valores_cartas(cartas_jugadores["jugador_1"][0], cartas_jugadores["jugador_1"][1]) == 9) and \
       (cm.carta_descubierta_crupier == ('2', 'Corazones')) or (cm.carta_descubierta_crupier == ('2', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('2', 'Treboles'))  or (cm.carta_descubierta_crupier == ('2', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('7', 'Corazones')) or (cm.carta_descubierta_crupier == ('7', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('7', 'Treboles'))  or (cm.carta_descubierta_crupier == ('7', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('8', 'Corazones')) or (cm.carta_descubierta_crupier == ('8', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('8', 'Treboles'))  or (cm.carta_descubierta_crupier == ('8', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('9', 'Corazones')) or (cm.carta_descubierta_crupier == ('9', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('9', 'Treboles'))  or (cm.carta_descubierta_crupier == ('9', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('A', 'Corazones')) or (cm.carta_descubierta_crupier == ('A', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('A', 'Treboles'))  or (cm.carta_descubierta_crupier == ('A', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('K', 'Corazones')) or (cm.carta_descubierta_crupier == ('K', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('K', 'Treboles'))  or (cm.carta_descubierta_crupier == ('K', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('J', 'Corazones')) or (cm.carta_descubierta_crupier == ('J', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('J', 'Treboles'))  or (cm.carta_descubierta_crupier == ('J', 'Picas') )or \
       (cm.carta_descubierta_crupier == ('Q', 'Corazones')) or (cm.carta_descubierta_crupier == ('Q', 'Diamantes'))or \
       (cm.carta_descubierta_crupier == ('Q', 'Treboles'))  or (cm.carta_descubierta_crupier == ('Q', 'Picas') ):
      print ("\n\nPedir Carta") 


    