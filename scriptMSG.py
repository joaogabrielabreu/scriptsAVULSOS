from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui 
import time

driver = webdriver.Chrome()

driver.get("https://x.com/i/flow/login?redirect_after_login=%2Fhome")
time.sleep(5)
elemento1 = driver.find_element(By.NAME, "text")


elemento1.send_keys("joãozinho123")#troque pelo seu usuário
pyautogui.press("enter")

time.sleep(2)
elemento2 = driver.find_element(By.NAME, "password")
elemento2.send_keys("senha123123") #troque pela sua senha
pyautogui.press("enter")

time.sleep(8)#tempo para carregar a página e não dar erro no código.

campoTexto = driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")

campoTexto.send_keys("Este é um tweet automatizado!")

try:
    #forma mais robusta de encontrar o elemento 
    botao_postar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButtonInline']"))
    )
    
    # Após encontrar o botão, clica nele
    botao_postar.click()
    
    print("Botão 'Postar' foi clicado com sucesso!")

except Exception as e:
    print(f"Não foi possível encontrar ou clicar no botão: {e}")
    

time.sleep(30)



driver.quit()

