from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

FIRST_SLIDER_LOCATOR = ("xpath", "(//div[@id='example-2']//div[@role='slider'])[1]")
SECOND_SLIDER_LOCATOR = ("xpath", "(//div[@id='example-2']//div[@role='slider'])[2]")

driver.get("https://seiyria.com/bootstrap-slider/#example-2")
slider_1 = driver.find_element(*FIRST_SLIDER_LOCATOR)
slider_2 = driver.find_element(*SECOND_SLIDER_LOCATOR)


def move_slider(current_position_attribute: str, endpoint: int, step: int | float, slider: WebElement):
    current_position = int(slider.get_attribute(current_position_attribute))
    if endpoint < current_position:
        offset = int((current_position - endpoint) / step)
        slider.send_keys(Keys.ARROW_LEFT * offset)
    elif endpoint > current_position:
        offset = int((endpoint - current_position) / step)
        slider.send_keys(Keys.ARROW_RIGHT * offset)


def set_range(
        first_slider: WebElement,
        second_slider: WebElement,
        target_positions: list, # [100, 200]
        current_position_attribute: str,
        step: int | float
):
    move_slider(current_position_attribute, target_positions[0], step, first_slider)
    move_slider(current_position_attribute, target_positions[1], step, second_slider)


time.sleep(3)
set_range(
    slider_1,
    slider_2,
    [200, 700],
    "aria-valuenow",
    1
)
time.sleep(3)
