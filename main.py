from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configurar o driver do navegador (certifique-se de que o driver está instalado e no PATH)
driver=webdriver.Chrome()

# Abrir a página web alvo
driver.get('https://www.omegle.com')

text = driver.find_element(By.ID,"textbtn").click()

time.sleep(10)

chatmsg = driver.find_element(By.CLASS_NAME,"chatmsg")

mensagem = "TESTE"
chatmsg.send_keys(mensagem)

chatmsg.send_keys(Keys.RETURN)

time.sleep(10000)