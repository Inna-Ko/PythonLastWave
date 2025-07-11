import requests
import pdfkit
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import subprocess


def download_page(url, html_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')

        for img in soup.find_all('img'):
            img['src'] = urljoin(url, img['src'])

        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"Страница успешно скачана в {html_file}.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании страницы: {e}")


def convert_to_pdf(html_file, pdf_file):
    try:
        options = {
            'enable-local-file-access': None,
            'disable-smart-shrinking': None,
            'no-stop-slow-scripts': None,
        }
        pdfkit.from_file(html_file, pdf_file, options=options)
        print(f"Конвертация завершена. PDF файл сохранен как {pdf_file}.")
    except Exception as e:
        print(f"Ошибка при конвертации в PDF: {e}")
        cmd = ['wkhtmltopdf', html_file, pdf_file]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Стандартный вывод:", result.stdout)
        print("Стандартный поток ошибок:", result.stderr)


if __name__ == "__main__":
    url = "https://www.google.com/"  # Замените на нужный URL
    html_file = "page.html"
    pdf_file = "output.pdf"

    download_page(url, html_file)
    convert_to_pdf(html_file, pdf_file)
