from datetime import datetime, timedelta

def calcular_proxima_revisao(dias):
    if dias < 0:
        raise ValueError("Dias não podem ser negativos")

    if dias > 30:
        raise ValueError("Valor muito alto para revisão")

    return datetime.now() + timedelta(days=dias)