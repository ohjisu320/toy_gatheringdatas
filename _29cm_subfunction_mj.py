# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# def getBrowserFromURI(uri):
#     webdriver_manager_directory = ChromeDriverManager().install()

#     # ChromeDriver 실행
#     browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

#     # Chrome WebDriver의 capabilities 속성 사용
#     capabilities = browser.capabilities

#     # - 주소 입력(https://www.w3schools.com/)
#     browser.get(uri)
#     return browser

# if __name__ == "__main__":
#     getBrowserFromURI(uri="https://www.29cm.co.kr/home/")
    
    
# browser = getBrowserFromURI(uri="https://www.29cm.co.kr/home/")

# from selenium.webdriver.common.by import By
# browser.find_element(by=By.CSS_SELECTOR, value="div.ng-tns-c43-0.nav_snb > div > ul > li:nth-child(1) > a").click()

# browser.quit()

# 주소 : https://www.29cm.co.kr/home/
# 상품 : __next > div.css-1k28ov0.e5a9ewn0 > div.css-1rr4qq7.e5a9ewn2 > ul > li:nth-child({}) > div > a
# 아이디(element_name) : div > div > div.css-cjqsv7.e1pl60v54 > span.css-5030pi.e1pl60v55
# 체형(element_bodytype) : 
# 사이즈(element_size) : 
# 리뷰(element_review) : 





# BEST -> 첫번째 상품 클릭 -> 
for x in [1,2,3,4] :
    #
    try :
        element_item = "__next > div.css-1k28ov0.e5a9ewn0 > div.css-1rr4qq7.e5a9ewn2 > ul > li:nth-child({}) > div > a".format(x)
        case_number = browser.find_element(by=By.CSS_SELECTOR, value="")
        case_number = case_number.text
    except :
        case_number = "None"


