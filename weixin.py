
from selenium import webdriver
import time
 
def RefreshReadingNum():
    url = '''https://mp.weixin.qq.com/s?__biz=MjM5MTYxNjQxOA==&mid=2652853736&idx=1&sn=7a89e8a6473c6250b5a8f8ef712726d2&chksm=bd5929258a2ea03314d533fe31138e9dc168d0360a7091a2354467e01d8affb87f3f8212b416&mpshare=1&scene=1&srcid=&sharer_sharetime=1583400043257&sharer_shareid=8a92a4ab7945b31f741de3c6000f1481&key=5f1294655622a3d55ccfaec11e24a3ae05486a6d154547e13b63acc8f739bbcc08d68a91fd8f1fa861c923dbfd812215a523ab1c8cf4aa4341a3fca50306513532553210b4201aea0e56a7a2d6d9705d&ascene=1&uin=MTc0NDg5NzMzNw%3D%3D&devicetype=Windows+10&version=62080079&lang=zh_CN&exportkey=AW6o4CJ4HmQR8Mq75JD50gU%3D&pass_ticket=Nt%2BAcFXWZRhK0YWMY7Zrxr6WaLoh%2FzYRRPR6aFWUPWm7ZKY5EhCW3EXqPdgAsOGj
    '''
    # 一共访问10W次
    for j in range(100000):
        # 实例化谷歌浏览器
        driver = webdriver.Chrome("chromedriver.exe")
        # 访问网站
        driver.get(url)
        # 设置搜索结果作为当前主窗口
        mainwindow = driver.current_window_handle
        # 搜索结果共有9篇文章
        for i in range(1,10):
            # 查找网页上的博客标题
            btn = driver.find_element_by_xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/h3/a'.format(i))
            driver.find_element_by_xpath('//h3[{}]/a'.format(i))
            # 模拟用户点击博客标题，从而进入博客界面
            btn.click()
            # 回到主窗口
            driver.switch_to.window(mainwindow)
            time.sleep(5)
        driver.close()
        time.sleep(120)
        driver.quit()
    print("结束！")
 
if __name__ == "__main__":
    RefreshReadingNum()