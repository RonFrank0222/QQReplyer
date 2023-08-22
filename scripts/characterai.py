from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#character=input("charname:")

def atri(msg):
    option=webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)
    #wait = WebDriverWait(browser, 60)

    #亚托利网址
    driver.get("https://beta.character.ai/chat?char=645T7h8NPizKNOHLKQiCKaT0htFgVwRfdpvrtdkHprU")
    #寻找输入框
    input_box=driver.find_element(By.CLASS_NAME,"input-group me-3 ms-3 my-0")
    input_box.sendKeys(msg)
    #寻找发送按钮
    send_button=driver.find_element(By.CLASS_NAME,"btn py-0")
    send_button.click()

if __name__=="__main__":
    atri("你好")