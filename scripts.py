def calc_imc(height, weight):
    """Calcula o IMC com base na altura e peso informados."""
    if height <= 0 or weight <= 0:
        raise ValueError("Altura e peso devem ser valores positivos.")
    
    imc = round(weight / (height * height), 1)  # Arredonda para 1 casa decimal
    return imc
