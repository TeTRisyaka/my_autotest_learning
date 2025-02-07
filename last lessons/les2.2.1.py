from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(int(x.text)+int(y.text)))
    input2 = browser.find_element(By.CSS_SELECTOR, "button")
    input2.click()
 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла