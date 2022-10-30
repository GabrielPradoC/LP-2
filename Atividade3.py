# coding=utf-8

def return_lowest_number(nums):
    """
    Retorna o menor número da lista

    :param nums: Lista de números
    :type nums: list
    :return: O menor número
    """
    nums.sort()
    return nums[0]


def prompt_ask_numbers():
    nums = []
    for x in range(3):
        nums.append(
            int(
                input("Insira um número: ")
            )
        )
    print("O menor número é: {0}".format(return_lowest_number(nums)))
