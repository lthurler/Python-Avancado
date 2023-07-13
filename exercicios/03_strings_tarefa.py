# strings e bytes não são diretamente intercambiáveis
# strings contém unicode, bytes são valores de 8 bits

def main():
    # definindo alguns valores iniciais
    b = bytes([0x41, 0x42, 0x43, 0x44])
    string = 'string'

    # TODO: Tente juntar os dois.
    # print(b + string)
    # TODO: Bytes e strings precisam ser apropriadamente encoded

    conjunto = string + b.decode('utf-8')
    print(conjunto)

    # TODO: Faça o encode da string como UTF-32

    conjunto = b + string.encode('utf-32')
    print(conjunto)


if __name__ == "__main__":
    main()
