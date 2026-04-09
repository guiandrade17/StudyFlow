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
            return dados.get("content", "Continue estudando, você está no caminho certo! 🚀")

        return "Continue estudando, você está no caminho certo! 🚀"

    except requests.exceptions.RequestException:
        return "Continue estudando, você está no caminho certo! 🚀"