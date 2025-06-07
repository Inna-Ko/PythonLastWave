from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

HORIZONTAL_SLIDER_LOCATOR = ("xpath", "(//div[@id='example-17']//div[@role='slider'])[1]")
VERTICAL_SLIDER_LOCATOR = ("xpath", "(//div[@id='example-17']//div[@role='slider'])[3]")

driver.get("https://seiyria.com/bootstrap-slider/#example-17")
slider_horizontal = driver.find_element(*HORIZONTAL_SLIDER_LOCATOR)
slider_vertical = driver.find_element(*VERTICAL_SLIDER_LOCATOR)


def move_horizontal_slider(current_position_attribute: str, endpoint: int, step: int | float, slider: WebElement):
    current_position = int(slider.get_attribute(current_position_attribute))
    if endpoint < current_position:
        offset = int((current_position - endpoint) / step)
        slider.send_keys(Keys.ARROW_LEFT * offset)
    elif endpoint > current_position:
        offset = int((endpoint - current_position) / step)
        slider.send_keys(Keys.ARROW_RIGHT * offset)


def move_vertical_slider(current_position_attribute: str, endpoint: int, step: int | float, slider: WebElement):
    current_position = int(slider.get_attribute(current_position_attribute))
    if endpoint < current_position:
        offset = int((current_position - endpoint) / step)
        slider.send_keys(Keys.ARROW_DOWN * offset)
    elif endpoint > current_position:
        offset = int((endpoint - current_position) / step)
        slider.send_keys(Keys.ARROW_UP * offset)


def set_value(
        slider: WebElement,
        current_position_attribute: str,
        target_position: int,
        step: int | float
):
    move_horizontal_slider(current_position_attribute, target_position, step, slider)


time.sleep(3)
set_value(
    slider_horizontal,
    "aria-valuenow",
    7,
    1
)
set_value(
    slider_vertical,
    "aria-valuenow",
    5,
    1
)

time.sleep(3)

