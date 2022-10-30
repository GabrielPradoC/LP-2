# coding=utf-8

def process_days(days):
    """
    Processa os dias informados e os retorna como anos, meses e dias

    :param days: Quantidade de dias
    :type days: int
    :return: Objeto com as propriedades anos, meses e dias
    """
    if type(days) != int:
        print("Por favor use apenas numeros")
        return {
            "years": 0,
            "months": 0,
            "days": 0
        }

    years = int(days/365)
    days_left = days % 365
    if days_left >= 30:
        months = int(days_left / 30)
        days = days_left % 30
        return {
            "years": years,
            "months": months,
            "days": days
        }
    else:
        days = days_left
        return {
            "years": years,
            "months": 0,
            "days": days
        }


def prompt_process_days():
    """
    Pergunta um número de dias e retorna o resultado formatado em anos, meses e dias
    """
    days = input("Informe a idade em dias:")
    result = process_days(days)
    print("Anos: {0}\nMeses: {1}\nDias: {2}".format(result["years"], result["months"], result["days"]))
