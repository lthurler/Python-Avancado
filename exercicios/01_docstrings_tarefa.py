# Usando docstrings para documentar métodos


def minha_funcao(param1, param2=None):
    """minha função para fazer print

    params:
        param1: Primeiro parametro. Função dele
        param2: Segundo parametro. Default: None. Função do parametro.
    """
    print(param1, param2)


def main():
    print(minha_funcao.__doc__)


if __name__ == "__main__":
    main()
