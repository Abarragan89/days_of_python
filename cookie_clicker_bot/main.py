from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Option to keep the window open after code has finished
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Choose Language
choose_language = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]'))
)
choose_language.click()

# Target Big Cookie
big_cookie = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# Product variables and counters
product1 = 0
product2 = 0
product3 = 0
product4 = 0
product5 = 0
product6 = 0
continue_game = True

while continue_game:
    big_cookie.click()

    # Get current cookie value
    cookies = driver.find_element(by=By.ID, value="cookies")
    cookies = cookies.text
    cookies = cookies.split(" ")[0]
    cookies = cookies.replace(",", "")
    cookies = int(cookies)

    # Get Three product 1
    if cookies > int(driver.find_element(by=By.ID, value="productPrice1").text) and product1 < 3:
        driver.find_element(by=By.ID, value="product1").click()
        product1 += 1

    # Get three product 2
    if product1 >= 3:
        product2_price = driver.find_element(by=By.ID, value="productPrice2").text
        product2_price = int(product2_price.replace(",", ""))
        # product2_price = int(product2_price)
        if cookies > product2_price and product2 < 3:
            driver.find_element(by=By.ID, value="product2").click()
            product2 += 1

    # Get Three product 3
    if product2 >= 3:
        product3_price = driver.find_element(by=By.ID, value="productPrice3").text
        product3_price = int(product3_price.replace(",", ""))
        if cookies > product3_price and product3 < 3:
            driver.find_element(by=By.ID, value="product3").click()
            product3 += 1

    # Get Three product 4
    if product3 >= 3:
        product4_price = driver.find_element(by=By.ID, value="productPrice4").text
        product4_price = int(product4_price.replace(",", ""))
        if cookies > product4_price and product4 < 3:
            driver.find_element(by=By.ID, value="product4").click()
            product4 += 1

    # Get three product 5
    if product4 >= 3:
        product5_price = driver.find_element(by=By.ID, value="productPrice5").text
        product5_price = int(product5_price.replace(",", ""))
        if cookies > product5_price and product5 < 3:
            driver.find_element(by=By.ID, value="product5").click()
            product5 += 1

    # Get three product 6
    if product5 >= 3:
        product6_price = driver.find_element(by=By.ID, value="productPrice6").text
        product6_price = int(product6_price.replace(",", ""))
        if cookies > product6_price and product6 < 3:
            driver.find_element(by=By.ID, value="product6").click()
            product6 += 1
    # End Game
    if product6 >= 3:
        continue_game = False
