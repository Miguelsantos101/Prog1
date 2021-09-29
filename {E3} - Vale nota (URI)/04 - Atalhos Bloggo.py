def negrito(letra, c_ne):
    if c_ne == 0:
        letra = "<b>"
        c_ne += 1
        return letra, c_ne

    if c_ne == 1:
        letra = "</b>"
        c_ne += -1
        return letra, c_ne


def italico(letra, c_it):
    if c_it == 0:
        letra = "<i>"
        c_it += 1
        return letra, c_it

    if c_it == 1:
        letra = "</i>"
        c_it += -1
        return letra, c_it


def verificar(texto):
    underline = "_"
    asterisk = "*"
    c_it = 0
    c_ne = 0
    for alpha in range(len(texto)):
        if texto[alpha] == underline:
            texto[alpha], c_it = italico(texto[alpha], c_it)

        if texto[alpha] == asterisk:
            texto[alpha], c_ne = negrito(texto[alpha], c_ne)

    return texto


def main():
    while True:
        try:
            texto = list(input())
            texto = verificar(texto)
            texto = "".join(texto)
            print(texto)
        except EOFError:
            break


main()

# def main():
#     while True:
#         try:
#             texto = list(input())
#             contador_it = 0
#             contador_ne = 0
#             for alpha in range(len(texto)):
#                 if texto[alpha] == "_" and contador_it == 0:
#                     texto[alpha] = "<i>"
#                     contador_it = contador_it + 1
#
#                 if texto[alpha] == "_" and contador_it == 1:
#                     texto[alpha] = "</i>"
#                     contador_it = contador_it - 1
#
#                 if texto[alpha] == "*" and contador_ne == 0:
#                     texto[alpha] = "<b>"
#                     contador_ne = contador_ne + 1
#
#                 if texto[alpha] == "*" and contador_ne == 1:
#                     texto[alpha] = "</b>"
#                     contador_ne = contador_ne - 1
#
#             texto = "".join(texto)
#             print(texto)
#         except EOFError:
#             break
#
#
# main()
