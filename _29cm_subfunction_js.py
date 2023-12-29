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

from selenium.webdriver.common.by import By
def reviews() :
    browser.switch_to.frame('')
    #__next > div.css-4djj0f.evt9g3e2 > section.eeja3je7.css-1w043rb.e16llo9z0 > div.css-0.e1fqypsc0 > ul > li> div > div
    list_reviews = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-cjqsv7.e1pl60v54 > span.css-5030pi.e1pl60v55")
    for num in range(len(list_reviews)) :
        list_ids = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-cjqsv7.e1pl60v54 > span.css-5030pi.e1pl60v55")
        list_body_type = []
        for x in range(len(list_reviews)):
            try :
                body_type = browser.find_element(by=By.CSS_SELECTOR, value="div > div:nth-child(1) > span.css-wle0cx.e1rsz3cb2").text
            except :
                body_type = ""
            list_body_type.append(body_type)
        list_size = browser.find_elements(by=By.CSS_SELECTOR, value="div > div:nth-child(2) > span.css-wle0cx.e1rsz3cb2")
        list_option = browser.find_elements(by=By.CSS_SELECTOR, value="div > div:nth-child(1) > span.css-wle0cx.e1rsz3cb2")
        list_contents = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-zeh8nu.e1pl60v57 > div.css-31l7gp.e1pl60v51 > p")
        toy_29cm.insert_one({"아이디": list_ids[num],"옵션": list_option[num],"사이즈": list_size[num], "체형": list_body_type[num],"내용":  list_contents[num]})
        pass

def reviews_test() :
    #__next > div.css-4djj0f.evt9g3e2 > section.eeja3je7.css-1w043rb.e16llo9z0 > div.css-0.e1fqypsc0 > ul > li> div > div
    list_reviews = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-cjqsv7.e1pl60v54 > span.css-5030pi.e1pl60v55")
   
    list_ids = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-cjqsv7.e1pl60v54 > span.css-5030pi.e1pl60v55")
    list_body_type = []

    body_type = browser.find_element(by=By.CSS_SELECTOR, value="div > div:nth-child(1) > span.css-wle0cx.e1rsz3cb2")

    list_body_type.append(body_type)
    list_size = browser.find_elements(by=By.CSS_SELECTOR, value="div > div:nth-child(2) > span.css-wle0cx.e1rsz3cb2")
    list_option = browser.find_elements(by=By.CSS_SELECTOR, value="div > div:nth-child(1) > span.css-wle0cx.e1rsz3cb2")
    list_contents = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-zeh8nu.e1pl60v57 > div.css-31l7gp.e1pl60v51 > p")
     
    
from pymongo import MongoClient
def Connect_Mongo(col_name):
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["gatheringdatas"]
    collection = database[col_name]
    collection.delete_many({})
    return collection

browser = getBrowserFromURI(uri="https://product.29cm.co.kr/catalog/1224495")
toy_29cm = Connect_Mongo("toy_29cm")
toy_29cm.insert_one({"아무개":"아무개"})
reviews_test()

# if __name__ == "__main__":
#     browser = getBrowserFromURI(uri="https://product.29cm.co.kr/catalog/1224495")
    