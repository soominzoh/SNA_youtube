from selenium import webdriver
import macro_get_title_n_ch
import txt_to_csv

driver=webdriver.Chrome(r'C:\Users\Z\Desktop\학교\youtubemacro\chromedriver')   
driver.get(r'https://www.youtube.com')

#after manual log-in
titlelist, chlist = macro_get_title_n_ch()

##########################################
## change file name after every trial ###
########################################

#save to txt
filename='보수01' #ex 진보03, 보수02
 
# used absolute path, change before saving 
import os

folder_path=r"C:\Users\Z\Desktop\학교\youtubemacro"
savepath=os.path.join(folder_path,str(filename+'.txt'))
f = open(savepath,'w', encoding='UTF8')
f.write(str(titlelist))
f.write('\n');f.write('\n');f.write('\n')
f.write(str(chlist))

f.close()


####### txt to csv conversion
txt_to_csv()

