import random

ataques = [
    ("látigo", 10, 5),
    ("placaje", 0, 10),
    ("pistola de agua", 20, 15),
]

ataques_oponente = [
    ("látigo", 10, 5),
    ("placaje", 0, 10),
    ("pistola de agua", 20, 15),
]

def elegir_ataque_jugador(ataques):
    while True:
        ataque_jugador = input("ataque: ").lower()
        ataque_encontrado = None
        for ataque in ataques:
            if ataque[0] == ataque_jugador:
                ataque_encontrado = ataque
                break
        if ataque_encontrado:
            break
        else:
            print("Cuidado, tus ataques son", [ataque[0] for ataque in ataques])
    return ataque_encontrado

def realizar_ataque(jugador, oponente, ataque):
    oponente[1] -= ataque[1]
    if oponente[0] <= 0:
        oponente[1] = 100
    oponente[0] -= ataque[2] / (1 + (oponente[1] / 100))
    print(f"El PS del oponente es: {oponente[0]}\nLa defensa del oponente es: {oponente[1]}")

def ataque_oponente_aleatorio(ataques_oponente):
    ataque_oponente = random.choice(ataques_oponente)
    print(f"El oponente ha realizado el ataque {ataque_oponente[0]}")
