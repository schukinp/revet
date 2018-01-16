from selenium import webdriver
import time

wd = webdriver.Chrome()


def registration():
    wd.get("https://dev2.revetinc.com/")
    wd.find_element_by_css_selector("a[href='/join-now/simple']").click()
    wd.find_element_by_css_selector("a[href='/join-now']").click()
    wd.find_element_by_css_selector("input[name='FirstName']").send_keys('QA')
    wd.find_element_by_css_selector("input[name='LastName']").send_keys('Engineer')
    wd.find_element_by_css_selector("input[name='UserName']").send_keys('test@example.com')
    wd.find_element_by_css_selector("input[name='Password']").send_keys('Qwerty1@')
    wd.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(3)
    wd.close()


registration()
