from datetime import datetime, timedelta

def calcular_proxima_revisao(dias):
    if dias < 0:
        raise ValueError("Dias não podem ser negativos")

    return datetime.now() + timedelta(days=dias)