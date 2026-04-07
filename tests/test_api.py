from src.core import obter_frase

def test_obter_frase_retorna_string():
    frase = obter_frase()

    assert isinstance(frase, str)
    assert len(frase) > 0