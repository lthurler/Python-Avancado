# Usando funções iteradoras como enumerate, zip, iter, next


def main():
    # Defina a lista de dias da semana em Português e English
    dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
    dias_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # TODO: Use a função iter para criar um iterador sobre uma lista
    iteradorDias = iter(dias)
    print(next(iteradorDias))
    print(next(iteradorDias))
    print(next(iteradorDias))
    print(next(iteradorDias))

    # TODO: Use uma função para iterar sobre um arquivo
    with open('exercicios/dados.txt', 'r') as pointer:
        for linha in iter(pointer.readline, ''):
            print(linha)
    # TODO: Use a iteração tradicional (range) sobre a lista dias
    for numero in range(len(dias)):
        print(numero, dias[numero])

    # TODO: Usar a função enumerate reduz a quantidade de código e te
    # dá um contador
    for numero, valor in enumerate(dias):
        print(numero, valor)
    # TODO: Use a função zip para combinar as listas
    for numero in zip(dias, dias_en):
        print(numero)

    # TODO: Combine zip com enumerate para formatar o resultado
    for index, valor in enumerate((zip(dias, dias_en))):
        print(index, valor[0], '=', valor[1], 'em inglês')


if __name__ == "__main__":
    main()
