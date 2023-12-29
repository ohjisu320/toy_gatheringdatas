from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

def getBrowserFromURI(uri):
    webdriver_manager_directory = ChromeDriverManager().install()

    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities

    browser.get(uri)
    return browser

def p_info(browser, bullsone_product) :
    time.sleep(2)
    p_name = browser.find_element(by=By.CSS_SELECTOR, value="#pdt2form > div > h3").text
    old = browser.find_elements(by=By.CSS_SELECTOR, value="#pdt2form > div > div.price_area > small > del")[0].text[4:]
    new = browser.find_elements(by=By.CSS_SELECTOR, value="#pdt2form > div > div.price_area > strong.price")[0].text
    star = browser.find_elements(by=By.CSS_SELECTOR, value="#pdt2form > div > div.about_rating > div > b")[0].text
    time.sleep(2)
    bullsone_product.insert_one({"상품명":p_name, "정상가": old, "할인가": new, "별점":star })
    return 




if __name__ == "__main__":
    from selenium.webdriver.common.by import By
    browser = getBrowserFromURI(uri="https://bullsonemall.com/store/product.detail.oz?pdtIdx=5423&cataIdx=")
    # 상품명 :#pdt2form > div > h3
    # 정상가 : #pdt2form > div > div.price_area > small > del
    # 할인가 : #pdt2form > div > div.price_area > strong.price
    # 별점 : #pdt2form > div > div.about_rating > div > b

    p_name = browser.find_element(by=By.CSS_SELECTOR, value="#pdt2form > div > h3").text
    old = browser.find_elements(by=By.CSS_SELECTOR, value="#pdt2form > div > div.price_area > small > del")[0].text[4:]
    new = browser.find_elements(by=By.CSS_SELECTOR, value="#pdt2form > div > div.price_area > strong.price")[0].text
    star = browser.find_elements(by=By.CSS_SELECTOR, value="#pdt2form > div > div.about_rating > div > b")[0].text
    from pymongo import MongoClient
    def Connect_Mongo(col_name):
        mongoClient = MongoClient("mongodb://localhost:27017")
        database = mongoClient["gatheringdatas"]
        collection = database[col_name]
        collection.delete_many({})
        return collection
    bullsone_product = Connect_Mongo("bullsone_product")
    bullsone_product.insert_one({"상품명":p_name , "정상가": old, "할인가": new, "별점":star })

# 주소 : https://bullsonemall.com
# 베스트 메뉴 : #header > section > section > ul > li:nth-child(2) > a
# 베스트 물품 : #best_list > div.item_list > div:nth-child({}) > dl > dt > a




# browser.quit()
