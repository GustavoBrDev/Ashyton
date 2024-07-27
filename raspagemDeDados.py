from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def checarAulas():
    elementos_aulas = navegador.find_elements(By.CSS_SELECTOR, 'tr.fc-list-item')
    if not elementos_aulas:
        return [], []
    else:
        aulas_tarde = set()
        aulas_noite = set()

        for aula in elementos_aulas:
            texto_aula = aula.find_element(By.CSS_SELECTOR, 'td.fc-list-item-title a').text.split('\n')

            if "18:00:00 - 19:00:00" <= texto_aula[3]:
                aulas_noite.add(tuple(texto_aula[:3]))
            else:
                aulas_tarde.add(tuple(texto_aula[:3]))

        return list(aulas_tarde), list(aulas_noite)


navegador = webdriver.Chrome()
navegador.get(url="https://estudante.sesisenai.org.br/login")

usuario = "usuario"
senha = "senha"

campoUsuario = navegador.find_element(By.NAME, "user")
campoUsuario.send_keys(usuario)

campoSenha = navegador.find_element(By.NAME, "password")
campoSenha.send_keys(senha)

navegador.find_element(By.TAG_NAME, "button").click()
# sleep(2)
botaoFechar = navegador.find_element(By.CSS_SELECTOR, 'button[data-v-79751d50][data-dismiss="modal"]')
# sleep(2)
botaoFechar.click()
# sleep(2)
navegador.find_element(By.CSS_SELECTOR, 'a[href="/quadro-horarios"]').click()
# sleep(2)
navegador.find_element(By.CSS_SELECTOR, 'button.fc-list-button').click()
# sleep(2)

navegador.find_element(By.CLASS_NAME, 'fc-icon-right-single-arrow').click()
navegador.find_element(By.CLASS_NAME, 'fc-icon-right-single-arrow').click()
navegador.find_element(By.CLASS_NAME, 'fc-icon-right-single-arrow').click()
navegador.find_element(By.CLASS_NAME, 'fc-icon-right-single-arrow').click()
navegador.find_element(By.CLASS_NAME, 'fc-icon-right-single-arrow').click()

sleep(2)


