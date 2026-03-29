import sys
import os
from datetime import datetime
import pytest

# Faz o Python encontrar o src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.core import calcular_proxima_revisao


# ✅ 1. CAMINHO FELIZ
def test_calculo_revisao_sucesso():
    resultado = calcular_proxima_revisao(3)
    assert isinstance(resultado, datetime)


# ❌ 2. ENTRADA INVÁLIDA
def test_erro_nivel_invalido():
    with pytest.raises(ValueError):
        calcular_proxima_revisao(-1)


# ⚠️ 3. CASO LIMITE
def test_zero_dias():
    resultado = calcular_proxima_revisao(0)
    assert isinstance(resultado, datetime)