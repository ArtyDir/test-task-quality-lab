from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def open_page_demoqa(driver):
    driver.get('https://demoqa.com/')
    # elements_btn = driver.find_element(By.XPATH, "//div[@class='card-body']//h5[text()='Elements']/../..")
    # elements_btn.click()


def open_page_elements(driver):
    driver.get('https://demoqa.com/elements')
    # test_box_btn = driver.find_elements(By.ID, 'item-0')
    # test_box_btn.click()


def open_page_text_box(driver):
    driver.get('https://demoqa.com/text-box')


def fill_text_box_form(driver, name, email, c_adress, p_adress):
    name_elem = driver.find_element(By.ID, 'userName')
    name_elem.send_keys(name)

    email_elem = driver.find_element(By.ID, 'userEmail')
    email_elem.send_keys(email)

    c_adress_elem = driver.find_element(By.ID, 'currentAddress')
    c_adress_elem.send_keys(c_adress)

    p_adress_elem = driver.find_element(By.ID, 'permanentAddress')
    p_adress_elem.send_keys(p_adress)

    btn_sub = driver.find_element(By.ID, 'submit')
    btn_sub.click()


def get_output_values(driver):
    out_name_elem = driver.find_element(By.ID, 'name')
    out_email_elem = driver.find_element(By.ID, 'email')
    out_c_adress_elem = driver.find_element(By.XPATH, "//p[@id='currentAddress']")
    out_p_adress_elem = driver.find_element(By.XPATH, "//p[@id='permanentAddress']")

    splitted_out_name_elem = out_name_elem.text.split(':')
    if len(splitted_out_name_elem) > 1:
        name1 = splitted_out_name_elem[1]
    else:
        name1 = ''

    splitted_out_email_elem = out_email_elem.text.split(':')
    if len(splitted_out_email_elem) > 1:
        email1 = splitted_out_email_elem[1]
    else:
        email1 = ''

    driver.save_screenshot('screen1.png')

    splitted_out_c_adress_elem = out_c_adress_elem.text.split(':')
    if len(splitted_out_c_adress_elem) > 1:
        c_adress1 = splitted_out_c_adress_elem[1]
    else:
        c_adress1 = ''
    print(out_p_adress_elem.text)

    splitted_out_p_adress_elem = out_p_adress_elem.text.split(':')
    if len(splitted_out_p_adress_elem) > 1:
        p_adress1 = splitted_out_p_adress_elem[1]
    else:
        p_adress1 = ''
    print(p_adress1)

    return name1, email1, c_adress1, p_adress1


options = Options()
options.add_argument('--headless')
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_size(2000, 1200)

name_v = 'Артём'
email_v = 'qqq@internet.ru'
c_adress_v = 'big street'
p_adress_v = 'small street'

open_page_demoqa(driver)
open_page_elements(driver)
open_page_text_box(driver)
fill_text_box_form(driver, name_v, email_v, c_adress_v, p_adress_v)
get_output_values(driver)

name, email, c_adress, p_adress = get_output_values(driver)

print(name)
print(email)
print(c_adress)
print(p_adress)

if name != name_v:
    print('Значения не равны!')
elif email != email_v:
    print('Значения не равны!')
elif c_adress != c_adress_v:
    print('Значения не равны!')
elif p_adress != p_adress_v:
    print('Значения не равны!')
else:
    print('Тест пройден!')
