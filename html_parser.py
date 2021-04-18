from selenium import webdriver

# webDriver应用程序路径
driverPath = r"D:\project\learn\python\chromedriver.exe"
wd = webdriver.Chrome(driverPath)
wd.implicitly_wait(5)

# 先登录
wd.get("https://www.nowcoder.com/login")
email_phone_input = wd.find_element_by_id("jsEmailIpt")
email_phone_input.send_keys("你的账号")
password_input = wd.find_element_by_id("jsPasswordIpt")
password_input.send_keys("密码")
login_button = wd.find_element_by_id("jsLoginBtn")
login_button.click()

# 打开URL文件
split = '===================================面经分割线==================================\n'
prefix = 'https://www.nowcoder.com'
for line in open("./url_almost_full.txt"):
    # 跳转到需要访问的页面
    line = line.replace('\n', '').replace('\r', '')
    print(prefix + line)
    script = 'window.open("' + prefix + line + '")'
    new_handle = wd.execute_script(script)
    main_handle = wd.current_window_handle
    handles = wd.window_handles
    for handle in handles:
        # 关闭登录跳转页面，转到面经页面
        if handle == main_handle:
            wd.close()
        else:
            wd.switch_to.window(handle)
    element = wd.find_element_by_css_selector(".post-topic-des")
    with open('./questions.txt', 'a', encoding='utf-8') as f:
        f.write(str(element.text) + '\n')
        f.write(split)
    print(element.text)