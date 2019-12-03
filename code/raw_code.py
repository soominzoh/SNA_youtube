from selenium import webdriver
import requests
import os; import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
### id zsm21375test@gmail.com
### pw z95s9m25

driver=webdriver.Chrome(r'C:\Users\Z\Desktop\학교\youtubemacro\chromedriver')   
time.sleep(1)
driver.get(r'https://www.youtube.com')
time.sleep(1)

# 로그인부터 한 다음에, 시작 영상 지정하고, 그 다음에 go 쳐넣기

x = input()
if x=='go':
    print('dasd')
    
print('lets get started')
#############################


titlelist=[]
chlist=[]
num=0
while True:  
    titlepath='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string'    
    title=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string').text
    ch=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/div[2]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a').text
    
    titlelist.append(title); chlist.append(ch)
    time.sleep(2) 
    
#따봉
    #driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon').click()

##category check
#    try:
#       driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/paper-button[2]/yt-formatted-string')\
#       .click()
#    except:
#        print('no 더보기 1')
        
#    try:
#        catpath=r"/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/ytd-metadata-row-container-renderer/div[2]/ytd-metadata-row-renderer/div/yt-formatted-string/a"
#        category=driver.find_element_by_xpath(catpath).text
#    except:
#       catpath2="/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/ytd-metadata-row-container-renderer/div[1]/ytd-metadata-row-renderer/div/yt-formatted-string/a"
#       category=driver.find_element_by_xpath(catpath2).text
##########
    
#다음 추천동영상 클릭
    #if up_category=='뉴스/정치':
    waypoint=driver.current_url
    waypoint=str(waypoint)
    
    #if category=='뉴스/정치':
     #   driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[12]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-autoplay-renderer/div[2]/ytd-compact-video-renderer/div[1]/div/div[1]/a/h3/span").click()
      #  time.sleep(4)
    
    indexer=1
    
    print(waypoint)
####################
    
    
    while True:
      
        top='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[12]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer['
        bottom=']/div[1]/div/div[1]/a/h3/span'
            
        driver.find_element_by_xpath(top+str(indexer)+bottom).click()
        indexer+=1
        ##category check
       
        
        ###로드될때까지 기다리기, 기준은 제목 로드
        WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, titlepath))
        )
        time.sleep(1)
        ###########
        try:
            duhbogi='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/paper-button[2]/yt-formatted-string'
            driver.find_element_by_xpath(duhbogi).click()
            break
        except:
            pass
                    
        try:
            catpath=r"/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/ytd-metadata-row-container-renderer/div[2]/ytd-metadata-row-renderer/div/yt-formatted-string/a"
            up_category=driver.find_element_by_xpath(catpath).text
        except:
            catpath2="/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/ytd-metadata-row-container-renderer/div[1]/ytd-metadata-row-renderer/div/yt-formatted-string/a"
            up_category=driver.find_element_by_xpath(catpath2).text
        ##########
        print(up_category)
        if ((up_category=='뉴스/정치')or(up_category=='인물/블로그')):
            previous_url = waypoint
            break
        else:
            
            #driver.back()
            driver.get(previous_url)
           
            time.sleep(3)
            
####################33
    print('while out')
        
    ####텍스트로 100마다 저장
    if num%100==0:
        f = open(r"C:\Users\Z\Desktop\학교\youtubemacro\진보03_trial"+(str(num))+".txt",'w', encoding='UTF8')
        f.write(str(titlelist))
        f.write('\n');f.write('\n');f.write('\n')
        f.write(str(chlist))

        f.close()
    ####
    #팝업탭 닫기
    driver.window_handles
    while len(driver.window_handles)!=1:
        
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        
        driver.close()    
    
    ###
    num=num+1


################################
# after manual break #
######################
    
f = open(r"C:\Users\Z\Desktop\학교\youtubemacro\진보03-03.txt",'w', encoding='UTF8')
f.write(str(titlelist))
f.write('\n');f.write('\n');f.write('\n')
f.write(str(chlist))

f.close()

print('ebd')
