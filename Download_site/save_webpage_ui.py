from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time


def save_webpage(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Содержимое сайта сохранено в файл: {filename}")


def download_links(driver, base_url):
    driver.get(base_url)
    time.sleep(3)  # Подождите, пока страница загрузится

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = set()

    # Извлечение всех ссылок
    for a in soup.find_all('a', href=True):
        link = a['href']
        if link.startswith('/'):
            link = base_url + link  # Преобразуем относительные ссылки в абсолютные
        if base_url in link:
            links.add(link)

    return links


def main():
    base_url = ""  # Замените на нужный URL
    username = ""  # Замените на ваше имя пользователя
    password = ""  # Замените на ваш пароль

    # Создаем директорию для сохранения страниц, если её нет
    os.makedirs('downloaded_pages', exist_ok=True)

    # Настройка Selenium
    driver = webdriver.Chrome()

    try:
        # Переход на страницу авторизации
        driver.get(base_url  + "/login")  # Замените на URL страницы входа
        time.sleep(3)  # Подождите, пока страница загрузится

        # Найдите поля ввода и кнопку для авторизации (замените селекторы на ваши)
        username_field = driver.find_element(By.NAME, "login")  # Измените селектор при необходимости
        password_field = driver.find_element(By.NAME, "password")  # Измените селектор при необходимости
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Измените селектор при необходимости

        # Вводим данные для входа
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        time.sleep(5)  # Подождите, пока произойдет вход

        # Сохраняем главную страницу
        print(driver.page_source)
        main_page_content = driver.page_source
        save_webpage(main_page_content, 'downloaded_pages/main_page.html')

        # Получаем ссылки второго уровня
        links = download_links(driver, base_url)

        # Сохраняем страницы по этим ссылкам
        for link in links:
            driver.get(link)
            time.sleep(3)  # Подождите, пока страница загрузится

            page_content = driver.page_source
            link_filename = f"downloaded_pages{link.replace(base_url, '').replace('/', '_')}.html"
            save_webpage(page_content, link_filename)

    finally:
        driver.quit()  # Закрываем браузер


if __name__ == "__main__":
    main()
