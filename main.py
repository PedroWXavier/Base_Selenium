import time

from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome()

    driver.get("https://selenium.dev")

    time.sleep(5)

    driver.quit()
