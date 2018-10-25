from bs4 import BeautifulSoup
import re
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
 


#must uncomment this wen extracting data from local html document
'''
raw_html = open('test.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
selected = html.select('a')

f= open("augusteighteen.txt","w+")
f.write(str(selected))
f.close()
'''

def main():	
    with open ("augusteighteen.txt","r") as f:
        data = f.read()
        
        match = re.findall (r""" (?:<a.+?>)(?P<name>\w+?\s?\w*?).\u2013. (?P<email>[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9])<""", data, re.X)
        
        names= [x[0] for x in match]
        emails = [x[1] for x in match]
          
    #now the code below writed email and names to excel
    df = pd.DataFrame({'Names':names, 'Emails':emails})
        
    writer = ExcelWriter('aug18openednl.xlsx',engine='xlsxwriter')
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()

main()




"""
#these few lines below extract emails from guru.txt
f = open("guru.txt", "r")
if f.mode == 'r':
    contents =f.read()    
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', contents)

"""