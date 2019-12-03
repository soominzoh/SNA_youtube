import os; import re; import pandas as pd; import numpy as np;

def txt_to_csv():
    path=r'C:\Users\Z\Desktop\학교\youtubemacro\usable'
    
    os.listdir(path)
        
    for i in os.listdir(path):
        if i.endswith('txt'):
            target=os.path.join(path,i)
            data=open(target, encoding='UTF8').read()   ### check encoding 
                
            data=data.split('\n\n\n')
            
            data[0]=data[0].split(',')
            data[1]=data[1].split(',')
            
            df = pd.DataFrame(data)
            
            df=df.transpose()
            
            prev=''
            link=''
            linklist=[]
            for i in data[1]:
                
                curr=i
                link=str(prev)+'-'+str(curr)
                linklist.append(link)
                
                prev=i
            
            df['edge']=pd.DataFrame(linklist)
            
            
            outpath=target[:-4]+'.csv'
            
            df.to_csv(outpath, mode='w', encoding='utf-8-sig', header=False)
    
    print('csv saved!')
     
        #            df.to_csv(outpath, mode='w',encoding='UTF8', header=False)
