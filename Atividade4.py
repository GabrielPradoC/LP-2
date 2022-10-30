# coding=utf-8

def is_prime(num):
    """
    Retorna se um número é primo ou não

    :param num: Número
    :type num: int
    :return: True ou false se o número é primo
    """
    if num == 1 | num == 0:
        return False

    for x in range(2, num):
        if num % x == 0:
            return False

    return True


def prompt_is_prime():
    number = input("Informe um número: ")
    print("O número informado {0} um número primo".format("é" if is_prime(number) else "não é"))