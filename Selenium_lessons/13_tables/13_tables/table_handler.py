from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

class TableHandler:

    _TABLE_LOCATOR = ("xpath", "//div[@role='table']")
    _ROWS_LOCATOR = ("xpath", ".//div[@role='row']")
    _CELLS_LOCATOR = ("xpath", ".//div[@role='cell']")
    _DELETE_BUTTON_LOCATOR = ("xpath", "//button[normalize-space()='Delete Selected']")
    _DOWNLOAD_BUTTON_LOCATOR = ("xpath", ".//button[.//i[contains(@class, 'bi-download')]]")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    @property
    def _table(self) -> WebElement:
        return self.driver.find_element(*self._TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self._ROWS_LOCATOR)

    @property
    def row_count(self):
        return len(self._rows)

    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.scroll_to_element(element).perform()

    def get_cell_content(self, row_number, column_number):
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self._CELLS_LOCATOR)[column_number - 1]
        return cell.text

    def get_row_content(self, row_number):
        row = self._rows[row_number - 1]
        return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]

    def select_row(self, row_number):
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self._CELLS_LOCATOR)[0]
        cell.click()

    def select_row_by_value(self, value: str):
        for index, row in enumerate(self._rows, start=1):
            if value in self.get_row_content(index):
                self.select_row(index)
                return
        raise ValueError("This value was not found in the table")

    def delete_row_by_value(self, value: str):
        for index, row in enumerate(self._rows, start=1):
            if value in self.get_row_content(index):
                self.select_row(index)
        delete_button = self.driver.find_element(*self._DELETE_BUTTON_LOCATOR)
        self.scroll_to_element(delete_button)
        delete_button.click()

    def download_by_first_value(self, value: str):
        for index, row in enumerate(self._rows, start=1):
            if value in self.get_row_content(index):
                row.find_element(*self._DOWNLOAD_BUTTON_LOCATOR).click()
                return
        raise ValueError("This value was not found in the table")
