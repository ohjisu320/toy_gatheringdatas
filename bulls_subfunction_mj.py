from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def getBrowserFromURI(uri):
    webdriver_manager_directory = ChromeDriverManager().install()

    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities

    # - 주소 입력(https://www.w3schools.com/)
    browser.get(uri)
    return browser

# if __name__ == "__main__":
#     getBrowserFromURI(uri="https://bullsonemall.com")


# 주소 : https://bullsonemall.com
# 베스트 메뉴 : #header > section > section > ul > li:nth-child(2) > a
# 베스트 물품 : #best_list > div.item_list > div:nth-child({}) > dl > dt > a




# browser.quit()
