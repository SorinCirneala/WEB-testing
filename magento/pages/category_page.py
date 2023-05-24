from locators import PRODUCT_INFO_BOX, SIZES, COLORS
from pages.base_page import BasePage


class CategoryPage(BasePage):
    # open the page, initializes the required variables
    def __init__(self):
        super().__init__()
        self.driver.maximize_window()
        self.driver.get("https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html")

    # page actions
    def get_products(self):
        products = self.get_all_elements(PRODUCT_INFO_BOX)
        return products

    def pick_a_size(self, size: str):
        self.click_element(SIZES[size])

    def pick_a_color(self, color: str):
        self.click_element(COLORS[color])

