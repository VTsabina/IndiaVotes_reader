from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import driver_path

chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # 0=все, 3=ошибки только

service = Service(executable_path=driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = 'https://www.indiavotes.com/alliance/partyWise/18/1'
    driver.get(url)

    wait = WebDriverWait(driver, 20)

    chart_div = wait.until(
        EC.presence_of_element_located((By.ID, 'charttable_alliance'))
    )

    table = chart_div.find_element(By.CLASS_NAME, 'grid')

    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td') or row.find_elements(By.TAG_NAME, 'th')
        row_texts = [cell.text for cell in cells]
        print(row_texts)

finally:
    driver.quit()


# from bs4 import BeautifulSoup
# import requests
# from constants import url, lok_sabha_num, state_codes, headers

# def get_result(year, states):
#     if len(states) == 0:
#         states=list(state_codes.keys())
#     for state in states:
#         addr = f'{url}/{year}/{state.lower().replace(' ', '-')}/{lok_sabha_num[year]}/{state_codes[state]}'
#         print(addr)
#         res = requests.get(addr, headers=headers)
#     return res

# def parser():
#     year = 0
#     while year < 1947 or year > 2024:
#         year = int(input('Enter year: '))
#     state_list = input('Enter states (sep by comma): ').split(', ')
#     res = get_result(year, state_list)
#     bs = BeautifulSoup(res.text, 'html.parser')
#     data = bs.find('div', class_="mianContent")
#     print(data)
#     # print(bs)


# if __name__ == '__main__':
#     parser()