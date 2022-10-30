# coding=utf-8

def invert_string(string):
    """
    Retorna a string informada invertida
    :param string: Frase ou palavra
    :type string: str
    :return: Frase ou palavra invertida
    """
    return string[::-1]


def prompt_invert_string():
    string = input("Informe uma frase: ")
    print("Frase invertida:\n{0}".format(invert_string(string)))
