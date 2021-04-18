import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# webDriver应用程序路径
driverPath = r"D:\project\learn\python\chromedriver.exe"
wd = webdriver.Chrome(driverPath)
wd.implicitly_wait(5)


# 如果不能登录，先看看网络通不通。检查本地wifi，ping牛客网等等
wd.get("https://www.nowcoder.com/login")
email_phone_input = wd.find_element_by_id("jsEmailIpt")
email_phone_input.send_keys("你的账号")
password_input = wd.find_element_by_id("jsPasswordIpt")
password_input.send_keys("你的密码")
login_button = wd.find_element_by_id("jsLoginBtn")
login_button.click()

# Java精选面经合集地址：https://www.nowcoder.com/discuss/experience?tagId=639
# 先获取到所有帖子的访问URL
new_handle = wd.execute_script('window.open("https://www.nowcoder.com/discuss/experience?tagId=639")')
main_handle = wd.current_window_handle
handles = wd.window_handles
for handle in handles:
    # 关闭登录跳转页面，转到面经页面
    if handle == main_handle:
        wd.close()
    else:
        wd.switch_to.window(handle)

# 滚动下拉动态获取帖子，目前只能拉取100页数据
page_num = 99
for i in range(page_num):
    # 刷新下一个响应
    # x=0,y=document.body.scrollHeight
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    ActionChains(wd).key_down(Keys.END).perform()
    time.sleep(5)

# 获取URL
elements = wd.find_elements_by_xpath("//ul[@class='column-best-list']/li")
for element in elements:
    # 追加存入文件中
    with open('./url.txt', 'a', encoding='utf-8') as f:
        f.write(str(element.get_attribute("data-href")) + '\n')











