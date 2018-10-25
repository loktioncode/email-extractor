import re
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

with open ("guru.txt", "r") as f:
    data = f.read()

match = re.findall (r"""(?:<a.+?>)(?P<name>\w+?\s?\w*?).\u2013.(?P<email>[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9])<""", data, re.X)



names= [x[0] for x in match]
emails = [x[1] for x in match]
asina_zita = []


match_email = re.findall(r"""[\w\.-]+@[\w\.-]+""", data)
for e in match_email:
    if e not in emails:
        asina_zita.append(e)
        

#now the code below writed email and names to excel
df = pd.DataFrame({'Names':names, 'Emails':emails}) 
writer = ExcelWriter('myemail.xlsx',engine='xlsxwriter')
df.to_excel(writer,'sheet 1',index=False)
writer.save()


#this writes all emails without name to new doc
df = pd.DataFrame({'NoName':asina_zita}) 
writer = ExcelWriter('noname.xlsx',engine='xlsxwriter')
df.to_excel(writer,'sheet 1',index=False)
writer.save()


print("Writing emails to excel sheet Done!")

print(len(asina_zita))


