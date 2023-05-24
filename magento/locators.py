from selenium.webdriver.common.by import By

# TODO: group locators in classes based on the page they are used on? or just use comment to organize them?


# login page
EMAIL_FIELD = (By.ID, "email")
PASS_FIELD = (By.ID, "pass")
SIGNIN_BTN = (By.ID, "send2")
PAGE_TITLE_LBL = (By.CLASS_NAME, "page-title")
ERROR_MSG = (By.CLASS_NAME, "message-error error message")

# category page
PRODUCT_INFO_BOX = (By.CLASS_NAME, "product-item-info")

# product and category page
SIZES = {
    "XS": (By.ID, "option-label-size-143-item-166"), 
    "S": (By.ID, "option-label-size-143-item-167"), 
    "M": (By.ID, "option-label-size-143-item-168"), 
    "L": (By.ID, "option-label-size-143-item-169"), 
    "XL": (By.ID, "option-label-size-143-item-170")
}

COLORS = {
    "black": (By.ID, "option-label-color-93-item-49"),
    "blue": (By.ID, "option-label-color-93-item-50"),
    "gray": (By.ID, "option-label-color-93-item-52"),
    "green": (By.ID, "option-label-color-93-item-53"),
    "orange": (By.ID, "option-label-color-93-item-56"),
    "purple": (By.ID, "option-label-color-93-item-57"),
    "red": (By.ID, "option-label-color-93-item-58"),
    "white": (By.ID, "option-label-color-93-item-59"),
    "yellow": (By.ID, "option-label-color-93-item-60"),
}