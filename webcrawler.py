from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.get("https://nckuhub.com/")
time.sleep(1)
index = ["序號", "名稱", "時間", "老師"]
data = []
courses = driver.find_elements(By.CLASS_NAME, "list_course_item_mid")
for course in courses:
    list1 = course.text.strip().split()
    if len(list1) != 7 or list1[0][0] != 'A' or list1[0][1] != '9':  # 先跳過缺資料的
        continue
    value = [list1[0], list1[1], list1[6], list1[4]]
    data.append(value)

df = pd.DataFrame(data, columns=index)
# df.to_csv("courseData.csv",index=False,encoding='utf-8')
print("Done.")


actions = ActionChains(driver)
pages = driver.find_elements(By.CLASS_NAME, 'list_course_item_description')
actions.move_by_offset(5, 5)
a=1
time.sleep(1)
for page in pages:
    # time.sleep(1)
    print("Course: ",a)
    a+=1
    page.click()
    # time.sleep(1)
    actions.click()
    actions.perform()

# x = driver.execute_script(
#     "return document.body.getBoundingClientRect().left;")
# print(x)


# for page in b:
#     page.click()
# driver.switch_to.frame(2)
# time.sleep(2)
# current_window = driver.current_window_handle
# time.sleep(2)
# print(b)
# driver.switch_to.window(main_window)
# time.sleep(2)

# 找到彈跳視窗的 handle
# for handle in driver.window_handles:
#     if handle != current_window:
#         popup_window = handle
#         break

# 切換到彈跳視窗
# driver.switch_to.window(popup_window)


# for point in points:
#     print(point.text)

# b.back()
# time.sleep(2)
# b.click()
# b.back()
# point = driver.find_element(By.CLASS_NAME, 'block_title').find_element(
#     By.CLASS_NAME, 'score-btn')
# print(point)
# driver.close()

# loop open try
# b = driver.find_elements(By.CLASS_NAME, 'list_course_item_description')
# for page in b:
#     page.click()
#     print(page.text.strip())
#     back=driver.find_element(By.CLASS_NAME,"hub_navbar__mobile__back_icon")
#     back.click()
print("All Done.")
driver.close()
