from selenium import webdriver
import time
import os.path
import multiprocessing as mp


def webshot(tup):
    print("当前进程%d已启动" % os.getpid())

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 不知为啥只能在无头模式执行才能截全屏
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # 返回网页的高度的js代码
    js_height = "return document.body.clientHeight"
    picname = str(tup[0])
    link = tup[1]
    print(link)

    driver.get('https://test.drims.cn/view/login.jsp')
    driver.implicitly_wait(10)
    print("login:")
    input_account = driver.find_element_by_id('login')
    input_account.send_keys('1004')
    print("password:")
    input_pwd = driver.find_element_by_id('password')
    input_pwd.send_keys('123456a')

    cookie = [item['name'] + '=' + item['value'] for item in driver.get_cookies()]
    print("start:",cookie)


    button_login = driver.find_element_by_css_selector("[class='btn btn-block btn-success']")
    # button_login = driver.find_element_by_link_text('登录')
    button_login.click()

    cookie = [item['name'] + '=' + item['value'] for item in driver.get_cookies()]
    print("get:",cookie)

    try:
        driver.get(link)
        k = 1
        height = driver.execute_script(js_height)
        while True:
            if k * 500 < height:
                js_move = "window.scrollTo(0,{})".format(k * 500)
                print(js_move)
                driver.execute_script(js_move)
                time.sleep(0.2)
                height = driver.execute_script(js_height)
                k += 1
            else:
                break
        scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(scroll_width, scroll_height)
        driver.get_screenshot_as_file("e:/phantomjstmp/pics/" + picname)
        print("Process {} get one pic !!!".format(os.getpid()))
        driver.quit()
    except Exception as e:
        print(picname, e)

def print_test():
    print("当前进程%d已启动" % os.getpid())

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get('https://test.drims.cn/view/login.jsp')
    while driver.execute_script("return document.getElementById('login')?false:true"):
        print('wait')
        time.sleep(0.1)


    print("login:")
    input_account = driver.find_element_by_id('login')
    input_account.send_keys('1004')
    print("password:")
    input_pwd = driver.find_element_by_id('password')
    input_pwd.send_keys('123456a')

    cookie = [item['name'] + '=' + item['value'] for item in driver.get_cookies()]
    print("start:",cookie)

    driver.execute_script("return document.getElementById('login')")


    button_login = driver.find_element_by_css_selector("[class='btn btn-block btn-success']")
    # button_login = driver.find_element_by_link_text('登录')
    button_login.click()

    cookie = [item['name'] + '=' + item['value'] for item in driver.get_cookies()]
    print("get:",cookie)


    driver.get('https://test.drims.cn/view/patient/patientDetail.jsp?id=368&type=1')
    time.sleep(0.3)
    while driver.execute_script("return typeof detailToday==='function'?detailToday('A368', 'rd_scale_physical', 309, '体格生长', 4313, '2021-08-05 15:43:55', 2119):true"):
        print('step1 wait')
        time.sleep(0.1)
    while driver.execute_script("return typeof printScale==='function'?printScale():true"):
        print('print window wait')
        time.sleep(0.1)

    while not driver.execute_script("return $('#popup_ok').length>0"):
        print('popup_ok wait')
        time.sleep(0.1)
    driver.execute_script("$('#popup_ok').trigger('click')")

    time.sleep(30)
    driver.quit()


if __name__ == '__main__':
    print_test()


    # filename = "e:/phantomjstmp/pics/"
    # if not os.path.isdir(filename):
    #     os.makedirs(filename)

    # 读取保存url的文件，返回一个列表
    # 列表中每个元素都是一个元组，文件保存url的格式是：保存为图片的名称, 网页地址。
    # 例：baidu.png,https://www.baidu.com
    #     zhihu.png,https://www.zhihu.com
    # with open('urls.txt', 'r') as f:
    #     lines = f.readlines()
    # lines = ['baidu.png,https://www.baidu.com']
    # urls = []
    # for line in lines:
    #     thelist = line.strip().split(",")
    #     if len(thelist) == 2 and thelist[0] and thelist[1]:
    #         urls.append((thelist[0], thelist[1]))

    # 创建进程池来多进程执行
    # pool = mp.Pool()
    # pool.map_async(func=webshot, iterable=urls)
    # pool.close()
    # pool.join()

    # webshot(('baidu.png','https://www.baidu.com'))
    # webshot(('drims_conner.png', 'https://test.drims.cn/view/preciousBaby/scale/rd_scale_conners.jsp?support=print&tableName=rd_scale_conners&tableDesc=Conners（父母问卷）&itemId=28&detailId=4023&printReporter=吕&printReporterId=3&printSign=8b3de1aa14e8453284f96b8333e01c9c&sendId=1853&visNo=A368&growPrint=undefined'))
    # webshot(('drims_zaoqi.png','https://test.drims.cn/view/preciousBaby/scale/rd_scale_rainbow.jsp?support=print&tableName=rd_scale_rainbow&tableDesc=%E5%84%BF%E7%AB%A5%E6%97%A9%E6%9C%9F%E5%8F%91%E5%B1%95%E8%AF%84%E4%BC%B0%E4%B8%8E%E5%85%BB%E8%82%B2%E6%8C%87%E5%AF%BC&itemId=1702&detailId=3864&printReporter=%E9%AB%98%E4%BD%93%E9%AA%8C&printReporterId=20&printSign=9b177b7e3faf4f2098652546d2d6d486&sendId=&visNo=A355&growPrint=undefined'))
    # webshot(('drims_zaoqi.png',''))

