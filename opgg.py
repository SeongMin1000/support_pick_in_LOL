from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import ImageGrab
from PIL import Image
import pytesseract
import pyperclip
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

###-------------------'''prtscr 버튼 누르기'''-------------###
BanPick_img=ImageGrab.grabclipboard() 
BanPick_img.save('lol.png','PNG') #롤 픽창화면 저장
img=Image.open('lol.png')
area=(200,660,567,900) #채팅창 자르기
Chat_img=img.crop(area)
Chat_img.show()

def Dodge_Jug(Name):
    webdriver_options=webdriver.ChromeOptions()
    webdriver_options.add_argument('headless')
    driver = webdriver.Chrome(options=webdriver_options)
    url = 'https://www.op.gg/summoner/userName=' + Name #닉네임 검색
    action = ActionChains(driver)
    driver.get(url)

    try:
        driver.find_element_by_css_selector('.Button.SemiRound.Blue').click() #갱신 버튼 클릭
        time.sleep(2)
        action.send_keys(Keys.ENTER) # 갱신 안 될 때 뜨는 alert '엔터키' 누르기고 확인
        driver.switch_to_alert().accept() #or 확인
        pass
        
    except:
        pass

    tier=driver.find_element_by_class_name("TierRank").text
    win=driver.find_element_by_class_name("wins").text
    lose=driver.find_element_by_class_name("losses").text
    winrate=driver.find_element_by_class_name("winratio").text
    return Name,tier,win,lose,winrate

print(Dodge_Jug('그노을'))##닉네임 입력


text = pytesseract.image_to_string(Chat_img,lang='kor+eng')##이미지 파일 글로 변환
print(text)

###닉네임 추출해서 리스트 만든 뒤 함수에 집어넣고 return 값을 각각 받아 
###클립보드에 복사하기


