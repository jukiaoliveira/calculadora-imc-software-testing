import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def iniciar_driver():
    driver = webdriver.Chrome()
    return driver

def test_fluxo_completo():
    """Testa o fluxo completo do sistema: entrada -> cálculo -> saída, com pausas para visualização"""

    driver = iniciar_driver()
    driver.get("file:///C:/Users/User/Desktop/Calculadora%20IMC/index.html")
    
    # Espera a página carregar completamente
    time.sleep(5)  

    # Encontrar os elementos de entrada
    height_input = driver.find_element(By.ID, "height")
    weight_input = driver.find_element(By.ID, "weight")
    calc_button = driver.find_element(By.ID, "calc-btn")

    # Limpar os campos antes de inserir novos valores
    height_input.clear()
    weight_input.clear()
    time.sleep(2)  # Pausa para visualizar os campos sendo limpos
    
    # Enviar os valores
    height_input.send_keys("1,75")
    time.sleep(2)  # Pausa para visualizar a digitação da altura
    weight_input.send_keys("70")
    time.sleep(2)  # Pausa para visualizar a digitação do peso
    
    # Clicar no botão de calcular usando JavaScript
    driver.execute_script("arguments[0].click();", calc_button)
    time.sleep(3)  # Tempo extra para visualizar o clique no botão

    # Esperar até que o resultado seja atualizado e não esteja vazio
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "imc-number").text.strip() != ""
    )

    # Capturar o resultado
    imc_element = driver.find_element(By.ID, "imc-number")
    imc_result = imc_element.text.strip()

    print(f"DEBUG - Resultado real exibido: '{imc_result}'")  
    time.sleep(5)  # Pausa final para observar o resultado antes de fechar o navegador

    # Verificar se o IMC calculado está correto
    assert "22.9" in imc_result  

    driver.quit()

test_fluxo_completo()
