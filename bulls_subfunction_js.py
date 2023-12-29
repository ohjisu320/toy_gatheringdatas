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

    # - 주소 입력
    browser.get(uri)
    return browser

from selenium.webdriver.common.by import By
def reviews() :
    #__next > div.css-4djj0f.evt9g3e2 > section.eeja3je7.css-1w043rb.e16llo9z0 > div.css-0.e1fqypsc0 > ul > li> div > div
    list_reviews = browser.find_elements(by=By.CSS_SELECTOR, value="#review_box > div.review_list.list_style01 > ul > li")
    list_names = browser.find_elements(by=By.CSS_SELECTOR, value="#review_box > div.review_list.list_style01 > ul > li > dl > dd.writer > span:nth-child(1)")
    list_special_reviews = []
    for reviews in list_reviews:
        try :
            special_reviews = reviews.find_element(by=By.CSS_SELECTOR, value="span.chip_box > span.chip_").text
            list_special_reviews.append(special_reviews)
        except :
            special_reviews = ""
        list_special_reviews.append(special_reviews)
    list_rate = browser.find_elements(by=By.CSS_SELECTOR, value="div.rating_stars.float-left > b ")
    list_contents = browser.find_elements(by=By.CSS_SELECTOR, value="div.review_list.list_style01 > ul > li > dl > dd.reply_view_inner > div.review_text > div")
    for num in range(len(list_reviews)) :
        bullsone_reviews.insert_one({"이름": list_names[num].text,"별점": list_rate[num].text,"네이버/한달사용": list_special_reviews[num],"내용":  list_contents[num].text})
        pass
    
from pymongo import MongoClient
def Connect_Mongo(col_name):
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["gatheringdatas"]
    collection = database[col_name]
    collection.delete_many({})
    return collection

browser = getBrowserFromURI(uri="https://bullsonemall.com/store/product.detail.oz?pdtIdx=5423&cataIdx=")
bullsone_reviews = Connect_Mongo("bullsone_reviews")
reviews()

# if __name__ == "__main__":
#     browser = getBrowserFromURI(uri="https://product.29cm.co.kr/catalog/1224495")
    