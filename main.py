import os
myFile=os.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Kaspersky Password Manager.exe",os.O_RDONLY)
myData=os.read(myFile,105)
myStr=myData.decode("UTF-8")
print(myStr)