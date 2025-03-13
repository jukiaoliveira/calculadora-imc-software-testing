import pytest
from scripts import calc_imc  # Importa a função do outro arquivo
# TESTE DE UNIDADE
def test_imc_valores_validos():
    """Testa se o cálculo do IMC está correto para entradas válidas."""
    assert calc_imc(1.75, 70) == 22.9
    assert calc_imc(1.60, 50) == 19.5
    assert calc_imc(1.80, 90) == 27.8

def test_imc_valores_invalidos():
    """Testa se valores inválidos levantam erro corretamente."""
    with pytest.raises(ValueError):
        calc_imc(0, 70)  # Altura não pode ser zero
    with pytest.raises(ValueError):
        calc_imc(1.75, -10)  # Peso não pode ser negativo
    with pytest.raises(ValueError):
        calc_imc(-1.75, 70)  # Altura negativa não pode existir
