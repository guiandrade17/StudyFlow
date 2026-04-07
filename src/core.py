from datetime import datetime, timedelta
import requests


def calcular_proxima_revisao(dias):
    if dias < 0:
        raise ValueError("Dias não podem ser negativos")

    return datetime.now() + timedelta(days=dias)


def obter_frase():
    url = "https://api.quotable.io/random"

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()
            return dados["content"]

        return "Não foi possível obter frase."

    except requests.exceptions.RequestException:
        return "Erro ao conectar com a API."