from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错

chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

'''
# jin10
browser = webdriver.Chrome("C:/Users/Administrator/Desktop/chromedriver.exe", options=chrome_options)
browser.get("https://xnews.jin10.com/details.html?id=21130")
# print(browser.page_source)

inputs = browser.find_elements(By.XPATH, "//*[@id=\"app\"]/div[3]/div/div/div[1]/div[5]/div[2]/p")
print(len(inputs))
for item in inputs:
    print('-->>>> ' + item.text)

time.sleep(3)
browser.close()

'''

# 火币网
browser = webdriver.Chrome("C:/Users/Administrator/Desktop/chromedriver.exe", options=chrome_options)
browser.get("https://www.huobi.co/zh-cn/markets/?nav=1")
# print(browser.page_source)

time.sleep(10)

inputs = browser.find_elements(By.XPATH, "//*[@id=\"symbol_list\"]/dd")
print(len(inputs))
for item in inputs:
    print('-->>>> ' + item.text)

browser.close()

