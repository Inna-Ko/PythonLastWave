from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

RED_SLIDER_LOCATOR = ("xpath", "(//div[@id='RC']//div[@role='slider'])[1]")
BLUE_SLIDER_LOCATOR = ("xpath", "(//div[@id='BC']//div[@role='slider'])[1]")
GREEN_SLIDER_LOCATOR = ("xpath", "(//div[@id='GC']//div[@role='slider'])[1]")
FINAL_COLOR_LOCATOR = ("xpath", "//div[@id='RGB']")

driver.get("https://seiyria.com/bootstrap-slider/#example-3")


def move_slider(current_position_attribute: str, endpoint: int, step: int | float, slider: WebElement):
    current_position = int(slider.get_attribute(current_position_attribute))
    if endpoint < current_position:
        offset = int((current_position - endpoint) / step)
        slider.send_keys(Keys.ARROW_LEFT * offset)
    elif endpoint > current_position:
        offset = int((endpoint - current_position) / step)
        slider.send_keys(Keys.ARROW_RIGHT * offset)


def set_rgb(red: int, green: int, blue: int):
    # Слайдеры для каждого цвета
    red_slider = driver.find_element(*RED_SLIDER_LOCATOR)
    green_slider = driver.find_element(*GREEN_SLIDER_LOCATOR)
    blue_slider = driver.find_element(*BLUE_SLIDER_LOCATOR)

    move_slider("aria-valuenow", red, 1, red_slider)
    move_slider("aria-valuenow", green, 1, green_slider)
    move_slider("aria-valuenow", blue, 1, blue_slider)

    final_color = driver.find_element(*FINAL_COLOR_LOCATOR).get_attribute("style")
    assert f"rgb({red}, {green}, {blue})" in final_color


time.sleep(3)
set_rgb(160, 160, 160)
time.sleep(5)
