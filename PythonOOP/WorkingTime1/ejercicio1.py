def sumatoria(numero):
    resultado = 0
    contador = 1
    while contador <= numero:
        resultado += contador
        contador += 1
    print(resultado)

sumatoria(100)