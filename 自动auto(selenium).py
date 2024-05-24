# import uuid,os
# a=[1,2,3]
# print(uuid.uuid4())

# print(a[-1])

# str=uuid.uuid4()
# print(str)
# print(str.hex)
# print(str.hex[:10])

# print(uuid.uuid4().hex[:10])

# file_path = os.path.join(r'media\files', 'file_name')
# print(file_path)

from selenium import webdriver
import time
 
# 实例化一款浏览器
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  #不自动关闭浏览器
# options.add_argument('--start-maximized')#浏览器窗口最大化
options.add_argument('--headless')#这个是后来隐藏的窗口 但是需要加上窗口的大小
options.add_argument('--window-size=1920,1080')  # 设置窗口大小为 1920x1080
chrome_driver = r'C:\Users\11608\Desktop\chromedriver-win32\chromedriver.exe' 
mychrome = webdriver.Chrome(executable_path = chrome_driver,options=options)

mychrome.get("https://www.mzyun.ren/")
# mychrome.send_keys('python selenium')
time.sleep(1)
mychrome.find_element_by_xpath('//*[@id="btn-area"]/span[4]').click()
# 
time.sleep(1)
mychrome.find_element_by_xpath('//*[@id="search-wd"]').send_keys('王杰')
time.sleep(1)
mychrome.find_element_by_xpath('//*[@id="search-area"]/div[1]/button').click()
time.sleep(1)
fetch=r'''var resp = fetch("https://www.amp360.net/inHtml/MusicPlayer/api.php?callback=jQuery1113011900341951858473_1654770566296", {
  "headers": {
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest"
  },
  "referrer": "https://www.amp360.net/inHtml/MusicPlayer/index.html",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "types=search&count=20&source=netease&pages=1&name=王菲",
  "method": "POST",
  "mode": "cors",
  "credentials": "omit"
});
return resp'''
resp = mychrome.execute_script(fetch)
#mychrome.execute_script(fetch) 是使用 Selenium WebDriver 的 execute_script() 方法来在 Chrome 浏览器上执行 JavaScript 代码。
print(resp)
# print(mychrome.page_source.encode('utf-8').decode('utf-8'))

# print("===================================")
# 获取请求头信息
# agent = mychrome.execute_script("return navigator.url")    
# print(agent)   # 查看请求头是否更改。
