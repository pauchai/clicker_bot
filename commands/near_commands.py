from . import Command
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
CFG_NEAR_URL = "https://near.org"

class CreateWalletCommand(Command):
    def __init__(self, bot_app ):
        self.bot_app = bot_app
    def execute(self):
        self.bot_app.webdriver.get(CFG_NEAR_URL)

        button = WebDriverWait(self.bot_app.webdriver, 10).until(
        EC.visibility_of_element_located((By.XPATH,'//button[.//*[contains(text(), "Create Account")]]' ))
        )
        button.click()
         # Находим <iframe> по CSS селектору
        iframe = WebDriverWait(self.bot_app.webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe"))
        )

        # Переключаемся на <iframe>
        self.bot_app.webdriver.switch_to.frame(iframe)

        email_input = WebDriverWait(self.bot_app.webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]'))
        )
        #username_input = WebDriverWait(self.bot_app.webdriver, 10).until(
        #    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-test-id="username_create"]'))
        #)
        #continue_button = WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="continue_button_create"]'))
        #)

        # Заполняем поля формы
        email_input.send_keys('user_name@email.com')
       # username_input.send_keys('user_name')

        # Кликаем по кнопке "Continue" для отправки формы
        #continue_button.click()