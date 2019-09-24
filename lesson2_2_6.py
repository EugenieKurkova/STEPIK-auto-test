from selenium import webdriver
import time

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y=calc(x)

    pasteplace = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", pasteplace)
    pasteplace.send_keys(y)

    button1=browser.find_element_by_id("robotCheckbox")
    button1.click()
    button2=browser.find_element_by_id(("robotsRule"))
    button2.click()

    buttonsubmit=browser.find_element_by_class_name("btn")
    buttonsubmit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
