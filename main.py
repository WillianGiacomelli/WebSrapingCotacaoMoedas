# Automação que pega valores de moedas e comoddities e atualiza planilha com base nessas cotações
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Seta o selenium para rodar em segundo plano e não abrir uma janela do navegador
option = webdriver.ChromeOptions()
option.add_argument('headless')
s
navegador =webdriver.Chrome(options=option)

# DÓLAR

# Acessa a URL no Chrome via instância da variável navegador
navegador.get('https://www.google.com/')

# Encontra o campo de busca do google e digita o texto para pesquisa
navegador.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')

# Aperta o enter após digitar o texto na barra de pesquisa
navegador.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element("xpath",'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print("Dólar: " + cotacao_dolar)

# EURO

navegador.get('https://www.google.com/')
navegador.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print("Euro:" + cotacao_euro)

# OURO

navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")
print("Ouro:" + cotacao_ouro)

navegador.quit()

