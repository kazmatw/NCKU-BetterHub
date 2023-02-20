from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains

# i use firefox beacause my os is linux 
driver = webdriver.Firefox()
driver.get("https://nckuhub.com/")

# apporiate time waiting can prevent program from bugs
time.sleep(1)

# index of pandas dataframe
index = ["序號", "名稱", "時間", "老師"]

# a list to collect course data
data = []

# beacause i can't get the point data, so i try to store all data i need in main page instead
courses = driver.find_elements(By.CLASS_NAME, "list_course_item_mid")

# i only collect data start with A9 which represents their the same kind of course
for course in courses:
    list1 = course.text.strip().split()
    if len(list1) != 7 or list1[0][0] != 'A' or list1[0][1] != '9':  # 先跳過缺資料的
        continue
    value = [list1[0], list1[1], list1[6], list1[4]]
    data.append(value)
df = pd.DataFrame(data, columns=index)

# and we save it as a csv file, we don't need to crawl it every time
# df.to_csv("courseData.csv",index=False,encoding='utf-8')
# after this work is done, i print a message to help me debug and check the status
print("Done.")


# now i'm going to traverse all the point page, cause this is the farest i can get
# first i store the click action in actionchains function, to help me exit the point page
actions = ActionChains(driver)
pages = driver.find_elements(By.CLASS_NAME, 'list_course_item_description')

# this location is near to the far left of the screen
actions.move_by_offset(5, 5)

# count rounds variable
a=1
time.sleep(2)

# it can work without any sleep sometimes, but most of the time 
# the page will not load completely and once we click too fast it will die
for page in pages:
    # time.sleep(1)
    print("Course: ",a)
    a+=1
    page.click()
    # time.sleep(1)
    actions.click()
    actions.perform()

# it can help you know your screen's far left(right)
# x = driver.execute_script(
#     "return document.body.getBoundingClientRect().left;")
# print(x)

print("All Done.")
driver.close()
