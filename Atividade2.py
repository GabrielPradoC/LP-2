# coding=utf-8

def check_triangle_sides(a, b, c):
    """
    Checa se é possível formar um triângulo com os tamanhos informados

    :param a: Lado 1
    :type a: int
    :param b: Lado 2
    :type b: int
    :param c: Lado 3
    :type c: int
    :return: True ou False se os lados formam um triângulo válido
    """
    return (
        a + b >= c and
        a + c >= b and
        b + c >= a
    )


def calculate_area(a, b, c):
    """
    Calcula a área do triângulo com os lados informados

    :param a: Lado 1
    :type a: int
    :param b: Lado 2
    :type b: int
    :param c: Lado 3
    :type c: int
    :return: Medida da área do triângulo
    """
    return (a + b + c)/2


def prompt_is_triangle():
    """
    Pede 3 valores e informa se eles formam um triângulo
    """
    print("Informe 3 valores")
    a = input("Valor 1: ")
    b = input("Valor 2: ")
    c = input("Valor 3: ")
    if check_triangle_sides(a, b, c):
        print("Area do triangulo: {0}".format(calculate_area(a + b + c)))
    else:
        print("Valores nao formam um triangulo\n {0} {1} {2}".format(a, b, c))
