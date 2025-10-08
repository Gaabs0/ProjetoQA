import pytest
from comparador import validar_prazo

def test_validar_prazo_financiamento_valido():
    assert validar_prazo(150, tipo='financiamento') == True

def test_validar_prazo_financiamento_invalido():
    with pytest.raises(ValueError):
        validar_prazo(150, tipo='financiamento')

def test_validar_prazo_consorcio_valido():
    assert validar_prazo(180, tipo='consorcio') == True

def test_validar_prazo_consorcio_invalido():
    with pytest.raises(ValueError):
        validar_prazo(200, tipo='consorcio')

 
 
import pytest
from comparador import validar_entrada

def test_entrada_valida():
    assert validar_entrada(valor_veiculo=10000, entrada=15000) == True

def test_entrada_minima_exata():
    assert validar_entrada(valor_veiculo=10000, entrada=10000) == True

def test_entrada_invalida():
    with pytest.raises(ValueError):
        validar_entrada(valor_veiculo=100000, entrada=9000)