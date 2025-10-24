cubo = lambda x: x**3

print(cubo(3))

delta = lambda a,b,c: b**2-4*a*c

print(delta(1, 12, -13))  

numeros = [1, -2, 3, 4, 5, 6, 7, 8, -9, -10, -123, 23,]
quadrado = lambda x: x * x
quadrados = list(map(quadrado, numeros))

print(quadrados) # saida: [1, 4, 9, 16, 25, 36,]

nomes = [coutinho , nobru, vanesa lopes, luana couto, jade lisboa, malevola, camila pudim, antonela braga, liz macedo, julia pimentel]
nomes_longos = list(filter(lambda nome: len(nome) > 5, nomes))

print(nomes_longos) # saida: ['luffy', 'seong gi-hun']b 