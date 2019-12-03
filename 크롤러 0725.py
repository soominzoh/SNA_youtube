from selenium import webdriver
import requests
import os; import re
import time


driver=webdriver.Chrome(r'C:\Users\pc3\Desktop\crawlingTEST\chromedriver')
driver.implicitly_wait(10)   

driver.get(r'https://klue.kr/')
driver.implicitly_wait(15)

time.sleep(3)
login = driver.find_element_by_xpath('/html/body/app-root/menubar/div/ul/menubar-guest/span[2]')
login.click()

user_id= driver.find_element_by_xpath('/html/body/app-root/app-modal/div/div/div/modal-contents/div/modal-login/input[1]')
user_id.send_keys('zsm21375')
pwd = driver.find_element_by_xpath('/html/body/app-root/app-modal/div/div/div/modal-contents/div/modal-login/input[2]')
pwd.send_keys('z95s9m25')
enter = driver.find_element_by_xpath('/html/body/app-root/app-modal/div/div/div/modal-contents/div/modal-login/button')
time.sleep(3)
enter.click()

openings = ['심리학의이해']

for key in openings:
    driver.get('https://klue.kr/lecture/search/'+key)
            
    stop_index = driver.find_element_by_xpath('/html/body/app-root/lecture-result/div/lecture-list/div/div[1]/span').text
    stop_index = int(stop_index)

    scroll_stop = (stop_index//10) + 1
        
    scrollcount=0
    while scrollcount < scroll_stop:
        driver.execute_script("window.scrollTo(90000, 160000);")
        scrollcount+=1
        print('scrollcount', scrollcount)
        time.sleep(1)
        driver.implicitly_wait(2)


    x= 3
    output=[]
    scrub=[]

    #아래는 실험용
    tester=[]
    while x <= stop_index+3:
        try: 

            semester=driver.find_element_by_xpath('/html/body/app-root/lecture-result/div/lecture-list/div/div['+str(x)+']/div[2]/div[1]/div[3]').text
            location=driver.find_element_by_xpath('/html/body/app-root/lecture-result/div/lecture-list/div/div['+str(x)+']/div[2]/div[1]/div[4]').text
            prof=driver.find_element_by_xpath('/html/body/app-root/lecture-result/div/lecture-list/div/div['+str(x)+']/div[2]/div[1]/div[2]/span[1]').text
            starscore=driver.find_element_by_xpath('/html/body/app-root/lecture-result/div/lecture-list/div/div['+str(x)+']/div[2]/div[1]/div[1]/span[3]').text

            fivescore=driver.find_element_by_xpath('/html/body/app-root/lecture-result/div/lecture-list/div/div['+str(x)+']/div[1]').text
            fivescore=fivescore.split('\n')[-5:]


            scrub=[semester, prof, starscore, fivescore]
            output.append(scrub)
                    
            tester.append(semester)

            print(x)
            x+=1
            
        except:
            print(f'{x}/{stop_index}에서 에러뜬다')
            x+=1
            
            
print(len(tester))
####
#텍스트파일로 출력


#set으로 교수명 불러와서 워드클라우드
"""
profset=set()
profset.append(prof)
안에 링크 들어가서 긁어오기.
"""
