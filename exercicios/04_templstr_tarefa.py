# Demonstração das funções de string templates
from string import Template


def main():
    # Formatação tradicional usando o método format()
    frase = "Você está assistindo {0} com {1}".format(
        "Python Avançado", "Jessica Temporal")
    print(frase)

    # TODO: Crie um template com placeholders
    tmplt = Template('Você está assistindo ${curso} com ${instrutora}')

    # TODO: Use o método substitute passando argumentos nomeados
    frase2 = tmplt.substitute(
        curso='python avançado',
        instrutora='Jessica Temporal'
    )
    print(frase2)

    # TODO: Use  o método substitute com um dicionário

    dados = {
        'curso': 'Python avançado',
        'instrutora': 'Jessica Temporal'
    }
    frase3 = tmplt.substitute(dados)
    print(frase3)


if __name__ == "__main__":
    main()
