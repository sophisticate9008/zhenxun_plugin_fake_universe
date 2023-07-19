# import random

# imprint_categories = [
#     ['刻印1', '刻印2', '刻印3'],
#     ['刻印4', '刻印5', '刻印6'],
#     ['刻印7', '刻印8', '刻印9']
# ]

# weights = [
#     3.0,
#     1.0,
#     2.0
# ]

# selected_imprints = []

# while len(set(selected_imprints)) < 3:
#     selected_imprints = random.choices(
#         [imprint for category in imprint_categories for imprint in category],
#         weights=[weight for weight, category in zip(weights, imprint_categories) for _ in range(len(category))],
#         k=3
#     )

# print(selected_imprints)
# class myclass:
#     a = [1, 2]
#     def get_a(self) :
#         b = self.a[:]

#         return b
#     def get(self):
#         b = self.get_a()
#         b[0] = 2
#         print(self.a)
#         print(b)
        
# a = myclass()

# a.get()

# a = {0:2}
# if a.get(0):
#     print(a.get(0))
#     b = a
#     b[0] = 3
#     print(a.get(0))
# import asyncio
# async def func1():

        
#     print(1)


# async def func2():
#     print(2)
    
# a = [func1, func2]




# import asyncio
# async def jishiqi1():
#     count = 0
#     while True:
        
#         await asyncio.sleep(1)
        
#         print("case1", count)
#         count += 1
# async def jishiqi2():
#     count = 0
#     while True:

#         await asyncio.sleep(1)
        
#         print("case2", count)
#         count += 1

# async_list = [jishiqi1(), jishiqi2()]
# async def main():
#     await asyncio.gather(*async_list)

# asyncio.run(main())

# f
# u_list = []
# for i in range(2):
#     u_list.append(str(i))
    
# text = "哈哈"
# for i in text:
#     print(i)
#     if i not in u_list:
#         print(111)
#         continue
#     print(222)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置Edge WebDriver的路径
webdriver_path = 'D:/7.file/file/msedgedriver.exe'  # 根据你的实际路径进行配置

# 创建Edge WebDriver实例
driver = webdriver.Edge()

# 打开网页
url = 'https://bbs.mihoyo.com/sr/wiki/content/767/detail?bbs_presentation_style=no_header'  # 替换为你要爬取的网页地址
driver.get(url)

# 使用显式等待，等待动态加载完成（根据实际情况调整等待时间）
wait = WebDriverWait(driver, 10)  # 设置最长等待时间为10秒
elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))

for element in elements:
    print(element.text)

elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))

for element in elements:
    if element.text != None:
        
        print(element.text)
        break



# 关闭浏览器窗口
driver.quit()




