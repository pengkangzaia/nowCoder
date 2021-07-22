import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# webDriver应用程序路径
driverPath = r"D:\project\learn\python\chromedriver.exe"
wd = webdriver.Chrome(driverPath)
wd.implicitly_wait(5)

# 先登录
wd.get("https://www.nowcoder.com/login")
tab_items = wd.find_elements_by_css_selector(".tab-item")
tab_items[1].click()
phone_password_input = wd.find_elements_by_css_selector(".el-input__inner")
phone_password_input[0].send_keys("15298372242")
phone_password_input[1].send_keys("qwe951951")
login_button = wd.find_element_by_css_selector(".el-button")
login_button.click()
after_login = wd.current_window_handle


# # Java精选面经合集地址：https://www.nowcoder.com/discuss/experience?tagId=639
# # 先获取到所有帖子的访问URL
# new_handle = wd.execute_script('window.open("https://www.nowcoder.com/discuss/experience?tagId=639&order=1&companyId=0&phaseId=1")')
# handles = wd.window_handles
# for handle in handles:
#     if handle != after_login:
#         wd.switch_to.window(handle)
#
# # 滚动下拉动态获取帖子，目前只能拉取100页数据
# page_num = 200
# for i in range(page_num):
#     # 刷新下一个响应
#     # x=0,y=document.body.scrollHeight
#     wd.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     ActionChains(wd).key_down(Keys.END).perform()
#     print("正在进行第" + str(i) + "页翻页")
#     time.sleep(0.5)
#
# # 获取URL
# elements = wd.find_elements_by_xpath("//ul[@class='column-best-list']/li")
# for element in elements:
#     # 追加存入文件中
#     with open('./url_20210721.txt', 'a', encoding='utf-8') as f:
#         f.write(str(element.get_attribute("data-href")) + '\n')
#
# # 关闭当前页面，转到登录后页面
# wd.close()
# wd.switch_to_window(after_login)

# 打开URL文件
split = '===================================面经分割线==================================\n'
prefix = 'https://www.nowcoder.com'
for line in open("./url_20210721.txt"):
    # 跳转到需要访问的页面
    line = line.replace('\n', '').replace('\r', '')
    print(prefix + line)
    script = 'window.open("' + prefix + line + '")'
    wd.execute_script(script)
    handles = wd.window_handles
    for handle in handles:
        if handle != after_login:
            wd.switch_to.window(handle)
            break
    element = wd.find_element_by_css_selector(".post-topic-des")
    title = wd.find_elements_by_css_selector(".post-title")
    with open('questions_20210721_bk.txt', 'a', encoding='utf-8') as f:
        f.write("{:=^100s}".format(str(title[0].text)) + '\n')
        f.write(str(element.text) + '\n')
        f.write("{:=^100s}".format("") + '\n')
    print(title[0].text)
    print(element.text)
    wd.close()
    wd.switch_to_window(after_login)
