import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
def check_elements():
    user_field = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    sub_button = driver.find_element(By.ID, "login-button")
    a = 1 if user_field.is_displayed() else 0
    b = 1 if password.is_displayed() else 0
    c = 1 if sub_button.is_displayed() else 0
    if a+b+c==3:
        print("Элементы найдены")
    print("Элементы найдены V2.0") if (user_field.is_displayed() and password.is_displayed() and sub_button.is_displayed())\
        else print("Элементы не найдены V2.0")

if __name__ == '__main__':
    check_elements()