import requests


def save_webpage(url, filename):
    try:
        # Отправляем GET-запрос к указанному URL
        response = requests.get(url)

        # Проверяем, успешно ли выполнен запрос
        if response.status_code == 200:
            # Сохраняем содержимое в файл
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Содержимое сайта сохранено в файл: {filename}")
        else:
            print(f"Не удалось загрузить страницу. Статус код: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример использования
url = "https://ya.ru/"  # Замените на нужный URL
filename = "downloaded_pages/webpage.html"  # Имя файла для сохранения
save_webpage(url, filename)
