from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configurar o driver do navegador (certifique-se de que o driver está instalado e no PATH)
driver=webdriver.Chrome()

# Abrir a página web alvo
driver.get('https://portal.dommus.com.br/login/morarmais')

# Localizar o elemento onde você deseja digitar a mensagem (você precisa inspecionar a página para encontrar o seletor correto)
elemento_de_mensagem = driver.find_element(By.ID, "cpf")

# Digitar a mensagem
mensagem = "038.443.772-98"
elemento_de_mensagem.send_keys(mensagem)

# Simular o pressionamento da tecla Enter (ou a ação apropriada para enviar a mensagem)
elemento_de_mensagem.send_keys(Keys.RETURN)

# Fechar o navegador após a conclusão
time.sleep(10000)

# Pressione a tecla Enter
elemento_de_mensagem.send_keys(Keys.RETURN)

# Repita o processo a cada 5 segundos
while True:
    time.sleep(5)
    elemento_de_mensagem.send_keys(Keys.RETURN)





