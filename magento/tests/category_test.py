import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

from time import sleep
from selenium.webdriver.remote.webelement import WebElement

from pages.category_page import CategoryPage
from locators import SIZES


# open a product page
def test_open_product_page():
    page = CategoryPage()
    products: list [WebElement] = page.get_products()
    products[2].click()
    sleep(2)

# select all size buttons
def test_select_each_size():
    page = CategoryPage()
    for size in SIZES.keys():
        page.pick_a_size(size)
        sleep(1)

# select a color
def test_select_a_color():
    page = CategoryPage()
    products: list [WebElement] = page.get_products()
    products[4].click()
    page.pick_a_color("red")
    sleep(2)

# add to cart

# add to whish list

