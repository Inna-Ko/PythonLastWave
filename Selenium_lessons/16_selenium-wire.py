from seleniumwire import webdriver

driver = webdriver.Chrome()
driver.get('https://httpbin.org/get')

for request in driver.requests:
    if request.response:
        print(request.method, request.url, request.response.status_code)

print('==============')

# ==============

driver.get('https://httpbin.org/forms/post')
driver.find_element('name', 'custname').send_keys('Alexey')
driver.find_element('tag name', 'form').submit()

# Найти POST-запрос
for request in driver.requests:
    if request.method == 'POST' and 'httpbin.org/post' in request.url:
        print('? Запрос:')
        print('URL:', request.url)
        print('Тело:', request.body.decode())
        print('? Ответ:')
        print('Код:', request.response.status_code)
        print('Ответ:', request.response.body.decode())