'''
Created on 2015年11月17日

@author: zhiwei
'''
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert 'Django' in browser.title