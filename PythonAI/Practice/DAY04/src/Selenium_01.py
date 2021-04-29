from selenium import webdriver

# 변수 선언
url_naver = "http://www.naver.com"
url_daum = "http://www.daum.net"
url_sugang = "https://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action"
CHROME_DRIVER = r"D:\download_program\Web Driver\chromedriver.exe"
CAP_IMG = '../data/website.png'


# 브라우저 드라이버 객체 생성
driver = webdriver.Chrome(CHROME_DRIVER)

# 브라우저 원격 제어 1
driver.implicitly_wait(1)           # 1초대기
driver.get(url_naver)               # URL 읽기
driver.save_screenshot(CAP_IMG)     # 화면캡처 & 저장
driver.get(url_daum)
driver.quit()                       # 브라우저 종료
