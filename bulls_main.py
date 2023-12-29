import bulls_subfunction_js as subfunction_js
import bulls_subfunction_mj as subfunction_mj
from selenium.webdriver.common.by import By
# 기본 function 형식 - 기다림. 불리울 때 기능한다. def function () : -> tap pass -> return 0
def main() :
    try:   # 업무 코드
        browser = subfunction_mj.getBrowserFromURI(uri="https://bullsonemall.com")  
        browser.find_element(by=By.CSS_SELECTOR, value="#header > section > section > ul > li:nth-child(2) > a").click()
        # loop_num=input("item number : ")
        for x in range(5) :
            try :
                # element_item = "#best_list > div.item_list > div:nth-child({}) > dl > dt > a".format(x)
                browser.find_element(by=By.CSS_SELECTOR, value="#best_list > div.item_list > div:nth-child({}) > dl > dt > a".format(x+2)).click()
                bullsone_reviews = subfunction_js.Connect_Mongo("bullsone_reviews")
                subfunction_js.reviews(browser=browser, bullsone_reviews=bullsone_reviews)
            except :
                pass
    except :
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass
    return 0

if __name__ == "__main__":
    try:
        main()    # 업무 코드
    except:
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass    # try나 except이 끝난 후 무조건 실행 코드