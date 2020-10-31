'''To send the message in a group'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip

driver=webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name=input('Enter the name of the user or the group: ')
pyperclip.copy(name)
l=[]
msg=input('Enter the message: ').strip().split()
while(len(msg)!=0):
    l.append(msg)
    msg=input().strip()
pyperclip.copy(msg)
searchbox= driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchbox.send_keys(name) 
searchbox.send_keys(Keys.ENTER) 
messagebox= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
for i in l:
    messagebox.send_keys(i) 
    messagebox.send_keys(Keys.ENTER) 
print("Message sent Successfully")
