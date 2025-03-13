import timeit
from scripts import calc_imc

def test_desempenho():
    """Testa se o cálculo do IMC é realizado rapidamente (menos de 0.01s)."""
    tempo_execucao = timeit.timeit(lambda: calc_imc(1.75, 70), number=1000) / 1000
    assert tempo_execucao < 0.01  # Espera que o cálculo leve menos de 10ms
