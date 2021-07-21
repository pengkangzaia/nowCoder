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

# 打开URL文件
split = '===================================面经分割线==================================\n'
prefix = 'https://www.nowcoder.com'
for line in open("./url_20210720.txt"):
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
    with open('./questions_20210720.txt', 'a', encoding='utf-8') as f:
        f.write('==============================' + str(title[0].text) + '===========================================\n')
        f.write(str(element.text) + '\n')
        f.write('============================================面经分割线===============================================\n')
    print(title[0].text)
    print(element.text)
    wd.close()
    wd.switch_to_window(after_login)
    # ActionChains(wd).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
