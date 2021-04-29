from selenium import webdriver
import time

# 변수 선언
url = "http://www.naver.com"
url_sugang = "https://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action"
CHROME_DRIVER = r"D:\download_program\Web Driver\chromedriver.exe"
CAP_IMG = '../data/website.png'

# 브라우저 드라이버 객체 생성
driver = webdriver.Chrome(CHROME_DRIVER)
# 브라우저 원격 제어 2
success = False
driver.get(url_sugang)
while True:
    # driver.find_element_by_xpath('//*[@id="query"]').send_keys("안녕하세요")
    driver.find_element_by_css_selector("#user\.stu_nbr").send_keys("2014104348")
    driver.find_element_by_css_selector("#user\.usr_id").send_keys("dfr456")
    driver.find_element_by_css_selector("#user\.passwd").send_keys("gjwosud0#21")
    driver.find_element_by_css_selector("#loginForm > table > tbody > tr:nth-child(4) > td > button.login").click()
    driver.implicitly_wait(2)
    start = time.time()
    while True :
        a=driver.find_element_by_css_selector("#lectPackReqGrid_0 > td.lect_req_cnt").text
        print(a)
        if(int(a)<250):
            driver.find_element_by_css_selector("#lectPackReqGrid_0 > td.button > a").click()
            success = True
            break
        driver.implicitly_wait(2000)
        driver.refresh()
        end = time.time()
        if(end-start>1000):
            break
    driver.find_element_by_css_selector("#logout > button.stop").click()
    if(success == True):
        break
driver.quit()
print("finish")