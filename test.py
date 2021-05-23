from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.op.gg/")
elem = driver.find_element_by_name("userName")#요소 찾기
elem.send_keys("###")#닉네임 입력 하기
elem.send_keys(Keys.RETURN)#엔터 입력
driver.find_element_by_class_name("Button.SemiRound.Blue").click()#갱신버튼 클릭   

##갱신 제한이 걸려있을 때 뜨는 alert를 자동으로 확인 버튼 누르고 
##넘어가는 코드를 작성해야 하는데 잘 되지 않습니다. 


tier=driver.find_element_by_class_name("TierRank").text
win=driver.find_element_by_class_name("wins").text
lose=driver.find_element_by_class_name("losses").text
winrate=driver.find_element_by_class_name("winratio").text
print('티어:'+tier+','+  winrate,'('+win,lose+')')
