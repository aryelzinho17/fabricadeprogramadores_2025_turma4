jogadores = [
    {'nome': 'playerOne', 'score': 1200, 'level': 15},
    {'nome': ' ninjaGui', 'score': 950, 'level': 12}
    {'nome': 'paiTaOFF', 'score': 200, 'level: 3}
    {'nome': 'Aninha_Gamer'', 'score': 1500, 'level: 18'},
    {'nome': 'Zezinho', 'score': 400, 'level': 5}
    ]

ranking = scorted(jogadores, key=lambda jogador: jogador['score'], reverse=True)
for jogador in ranking:
    print(jogadorz)    