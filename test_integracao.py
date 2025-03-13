from scripts import calc_imc

def test_integração_inputs():
    """Testa se os valores digitados pelo usuário são corretamente convertidos para a função de cálculo."""
    altura = "1.75"
    peso = "70"

    # Simula a conversão dos inputs do formulário para float
    altura_float = float(altura.replace(",", "."))
    peso_float = float(peso.replace(",", "."))

    resultado = calc_imc(altura_float, peso_float)

    assert resultado == 22.9  # Confere se o cálculo bate com o esperado
