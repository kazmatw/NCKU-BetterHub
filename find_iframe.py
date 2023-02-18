from selenium import webdriver

# 載入網頁
driver = webdriver.Firefox()

driver.get('https://nckuhub.com/')

# 列出所有 iframe 的 ID 和名稱
iframes = driver.find_elements_by_tag_name('iframe')
for iframe in iframes:
    print('ID: ', iframe.get_attribute('id'))
    print('Name: ', iframe.get_attribute('name'))

# 關閉瀏覽器視窗
driver.quit()
