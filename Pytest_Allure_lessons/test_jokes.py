from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestJokes:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

        # Логин на сайт
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys("Admin")

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("admin123")

        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Ожидание успешного входа
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-main-menu"))
        )

    def teardown_method(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

    def test_post_joke(self, get_joke):
        buzz_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
        buzz_link.click()

        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-buzz-post-input")))
        time.sleep(3)
        post_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.oxd-buzz-post-input")))
        post_input.click()
        post_input.send_keys(get_joke)

        share_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        share_button.click()

        time.sleep(3)

        self.driver.refresh()
        posts = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "orangehrm-buzz-post-body-text")))
        latest_post = posts[0]
        post_text = latest_post.text

        assert post_text in get_joke, f"Шутка не найдена в посте. Ожидалось: {get_joke}, Найдено: {post_text}"
        print(f"Тест пройден! Шутка успешно размещена: {get_joke[:50]}...")
