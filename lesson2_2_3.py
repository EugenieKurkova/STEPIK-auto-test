from selenium import webdriver
import time

try:
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x=browser.find_element_by_id('num1')
    x1=x.text
    y=browser.find_element_by_id('num2')
    y1=y.text
    sum1=int(x1)+int(y1)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum1)) # ищем элемент с текстом "Python"


    buttonsubmit=browser.find_element_by_class_name("btn")
    buttonsubmit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
