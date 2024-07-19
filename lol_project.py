from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import ImageGrab
from PIL import Image
import pytesseract
import pyperclip 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# 롤 픽창 들어가면 먼저 prtscr버튼 눌러야함

BanPick_img=ImageGrab.grabclipboard() 
BanPick_img.save('lol.png','PNG') #롤 픽창화면 저장
img=Image.open('lol.png')
area=(200,660,567,900) # 채팅창 픽셀에 맞춰 자르기
Chat_img=img.crop(area)

webdriver_options=webdriver.ChromeOptions()
webdriver_options.add_argument('headless')
driver = webdriver.Chrome(options=webdriver_options)

def Dodge_Jug(Name):
    
    url = 'https://www.op.gg/summoner/userName=' + Name # 닉네임 검색
    action = ActionChains(driver)
    driver.get(url)

    try:
        driver.find_element_by_css_selector('.Button.SemiRound.Blue').click() # 갱신 버튼 클릭
        time.sleep(2)
        action.send_keys(Keys.ENTER) # 최근 갱신 3분미만 일 때 뜨는 alert '엔터키' 누르고 확인
        driver.switch_to_alert().accept() #''''''
        pass
    
    except:
        pass

    tier=driver.find_element_by_class_name("TierRank").text
    win=driver.find_element_by_class_name("wins").text
    lose=driver.find_element_by_class_name("losses").text
    winrate=driver.find_element_by_class_name("winratio").text
    
    result='%s(%s): %s (%s,%s)' %(Name, tier, winrate, win, lose)
    #------반복문 실행할 때 켜진 창 끄고 새로운 창 띄우기------#
    driver.execute_script('window.open();')
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    #-------------------------------------------------------#
    return result

# 이미지 파일 글로 변환
msg = pytesseract.image_to_string(Chat_img,lang='kor+eng').split('\n')

Name_list=[]

# 닉네임만 추출
for w in msg:
    if '로비에' in w:
        Nick=w[0:w.index('로비에')-3]
        if (Nick) not in Name_list:
            Name_list.append(Nick) 

team_luck=''
for i in Name_list:
    team_luck+='%s\n'%(Dodge_Jug(i))

pyperclip.copy(chat) # 결과값 클립보드에 복사

#>>>>픽창에 그대로 복붙하면 됨
