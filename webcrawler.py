from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get("https://nckuhub.com/")
time.sleep(2)
index = ["序號", "名稱", "時間", "老師"]
data = []
courses = driver.find_elements(By.CLASS_NAME, "list_course_item_mid")
for course in courses:
    list1 = course.text.strip().split()
    if len(list1) != 7 or list1[0][0]!='A' or list1[0][1]!='9':  # 先跳過缺資料的
        continue
    value = [list1[0], list1[1], list1[6], list1[4]]
    data.append(value)

df = pd.DataFrame(data, columns=index)
df.to_csv("courseData.csv",index=False,encoding='utf-8')
print("Done.")
time.sleep(2)
driver.close()
