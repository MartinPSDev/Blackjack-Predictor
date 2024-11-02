from .common_utils import*
import common_utils as cm

def sumar_valores_cartas(primera_carta_jugador,segunda_carta_jugador):
    # Asumiendo que primera_carta_jugador y segunda_carta_jugador están definidas y accesibles
    valor_primera_carta = int(primera_carta_jugador[0][0])  # Convierte el número de la primera carta a entero
    valor_segunda_carta = int(segunda_carta_jugador[0][0])  # Convierte el número de la segunda carta a entero
    
    suma = valor_primera_carta + valor_segunda_carta
    return suma

def estrategia_basica():
    # Simplificación de la lógica para pedir carta
    valor_cartas_jugador = sumar_valores_cartas(cartas_jugadores["jugador_1"][0], cartas_jugadores["jugador_1"][1])
    
    if valor_cartas_jugador < 12:
        print("\n\nPedir Carta")
    elif valor_cartas_jugador == 12 and cm.carta_descubierta_crupier in [('4', 'Corazones'), ('4', 'Diamantes'), ('4', 'Treboles'), ('4', 'Picas'),
                                                                         ('5', 'Corazones'), ('5', 'Diamantes'), ('5', 'Treboles'), ('5', 'Picas'),
                                                                         ('6', 'Corazones'), ('6', 'Diamantes'), ('6', 'Treboles'), ('6', 'Picas')]:
        print("\n\nNo Pedir Carta")
    elif valor_cartas_jugador >= 13 and valor_cartas_jugador <= 16 and cm.carta_descubierta_crupier in [('7', 'Corazones'), ('7', 'Diamantes'), ('7', 'Treboles'), ('7', 'Picas'),
                                                                                                          ('8', 'Corazones'), ('8', 'Diamantes'), ('8', 'Treboles'), ('8', 'Picas'),
                                                                                                          ('9', 'Corazones'), ('9', 'Diamantes'), ('9', 'Treboles'), ('9', 'Picas'),
                                                                                                          ('10', 'Corazones'), ('10', 'Diamantes'), ('10', 'Treboles'), ('10', 'Picas'),
                                                                                                          ('A', 'Corazones'), ('A', 'Diamantes'), ('A', 'Treboles'), ('A', 'Picas')]:
        print("\n\nPedir Carta")
    else:
        print("\n\nNo Pedir Carta")