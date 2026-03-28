from src.core import calcular_proxima_revisao
from datetime import datetime
import pytest

def test_calculo_revisao_sucesso():
    resultado = calcular_proxima_revisao(1)
    assert isinstance(resultado, datetime)

def test_erro_valor_negativo():
    with pytest.raises(ValueError):
        calcular_proxima_revisao(-1)