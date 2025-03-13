from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar WebDriver
driver = webdriver.Chrome()

def test_fluxo_completo():
    """Testa o fluxo completo do sistema: entrada -> cálculo -> saída"""
    driver.get("file:///C:/Users/User/Desktop/Calculadora%20IMC/index.html")  # Verifique o caminho correto

    time.sleep(2)  # Espera 2 segundos para garantir que a página carregou

    # Agora encontra os campos corretamente
    height_input = driver.find_element(By.ID, "height")
    weight_input = driver.find_element(By.ID, "weight")
    calc_button = driver.find_element(By.ID, "calc-btn")

    height_input.send_keys("1.75")
    height_input.send_keys(Keys.RETURN)  # Pressiona Enter para confirmar a entrada
    weight_input.send_keys("70")
    weight_input.send_keys(Keys.RETURN)  # Pressiona Enter para confirmar a entrada

    calc_button.click()  # Clica no botão de cálculo

    time.sleep(2)  # Espera o resultado aparecer

    # Captura o resultado exibido na tela
    imc_result = driver.find_element(By.ID, "imc-number").text
    print(f"IMC retornado pelo sistema: {imc_result}")  # Para depuração
    assert "22.9" in imc_result  # Verifica se o IMC calculado foi correto

    driver.quit()
