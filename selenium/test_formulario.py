import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL_APP = "http://localhost:5173"


class TestFormularioReact(unittest.TestCase):
    def setUp(self):
        # Selenium Manager procura ou gerencia o driver do navegador.
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.get(URL_APP)

        # Aguarda a aplicação React exibir o campo antes de começar.
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "titulo"))
        )

    def tearDown(self):
        # Fecha o navegador ao final de cada teste.
        if hasattr(self, "driver"):
            self.driver.quit()

    def test_salva_titulo_e_exibe_confirmacao(self):
        campo_titulo = self.driver.find_element(By.ID, "titulo")
        campo_titulo.send_keys("Teste Selenium")

        botao_salvar = self.driver.find_element(
            By.CSS_SELECTOR,
            '[data-testid="acao-principal"]'
        )
        botao_salvar.click()

        mensagem = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[role="status"]')
            )
        )

        self.assertEqual(mensagem.text, "Salvo: Teste Selenium")
        self.assertEqual(campo_titulo.get_attribute("value"), "")

    def test_campo_vazio_exibe_mensagem_de_erro(self):
        botao_salvar = self.driver.find_element(
            By.CSS_SELECTOR,
            '[data-testid="acao-principal"]'
        )
        botao_salvar.click()

        mensagem = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[role="alert"]')
            )
        )

        self.assertEqual(mensagem.text, "O título é obrigatório.")

        campo_titulo = self.driver.find_element(By.ID, "titulo")
        self.assertEqual(
            campo_titulo.get_attribute("aria-invalid"),
            "true"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)