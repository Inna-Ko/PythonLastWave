from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class TableHandler:

    _TABLE_LOCATOR = ("xpath", "//div[@role='table']")
    _ROWS_LOCATOR = ("xpath", ".//div[@class='oxd-table-card']//div[@role='row']")
    _CELLS_LOCATOR = ("xpath", ".//div[@role='cell']")
    _DELETE_BUTTON_LOCATOR = ("xpath", ".//div[@class='oxd-table-cell-actions']//button[.//i[contains(@class, 'bi-trash')]]")
    _EDIT_BUTTON_LOCATOR = ("xpath", ".//div[@class='oxd-table-cell-actions']//button[.//i[contains(@class, 'bi-pencil-fill')]]")

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

    def get_cell_content(self, row_number, column_number):
        row = self._rows[row_number - 1] # rows[4]
        cell = row.find_elements(*self._CELLS_LOCATOR)[column_number - 1]
        return cell.text

    def get_row_content(self, row_number):
        # Пример с list compr
        row = self._rows[row_number - 1]
        return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]

    def get_column_content(self, column_number):
        # Пример без list compr
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self._CELLS_LOCATOR)
            column_content.append(cells[column_number - 1].text)
        return column_content

    def select_row(self, row_number):
        row = self._rows[row_number - 1]
        if "Admin" in self.get_row_content(row_number):
            raise AssertionError("YOU SHALL NOT PASS")
        else:
            cell = row.find_elements(*self._CELLS_LOCATOR)[0]
            cell.click()

    def select_by_username(self, username: str):
        for index, row in enumerate(self._rows, start=1): # ["", "", ""]
            if username in self.get_row_content(index):
                self.select_row(index)
                return
        raise ValueError("This user was not found in the table")

    def delete_by_username(self, username: str):
        for index, row in enumerate(self._rows, start=1):  # ["", "", ""]
            if username in self.get_row_content(index):
                row.find_element(*self._DELETE_BUTTON_LOCATOR).click()
                return
        raise ValueError("This user was not found in the table")

    def edit_by_username(self, username: str):
        for index, row in enumerate(self._rows, start=1):  # ["", "", ""]
            if username in self.get_row_content(index):
                row.find_element(*self._EDIT_BUTTON_LOCATOR).click()
                return
        raise ValueError("This user was not found in the table")