""" Однопоточный парсер ссылок, и загрузчик видео с помощью selenium"""
from selenium import webdriver
import time
import re
import math


# Создаёт список ссылок на видео по ключевому слову
def getListVideoHref(searchkey='lolly'):
    url = 'https://www.xnxx.com/'
    browser.get(url)

    # Отправить ключевое слово
    search = browser.find_element_by_xpath('//*[@id="k"]')
    search.send_keys(searchkey)

    # Нажать на поиск
    search = browser.find_element_by_xpath('//*[@id="xnxx-search-bar"]/button[2]')
    search.click()

    startTime = time.time()
    # Подсчет страниц (около 37 видео на странице)
    try:
        continue_link = browser.find_element_by_xpath("//*[@id='content-thumbs']/div[1]").text
        pageNum = math.ceil(int(re.sub("\D", "", continue_link)) // 37) + 5
    except:
        pageNum = 1000

    # Генерация ссылок
    search_url = 'https://www.xnxx.com/search/' + searchkey + '/'
    pageList = [search_url + str(i) for i in range(pageNum)]

    hrefList = []
    # Перейти к каждой странице, чтобы получить ссылки видео
    for url_p in pageList:
        try:
            browser.get(url_p)
            continue_link = browser.find_elements_by_xpath("//div[@class='thumb-under']/p/a")
            for i in range(len(continue_link)):
                hrefList.append(continue_link[i].get_attribute('href'))
        except:
            pass
        break
    print('Время выполнения: %.1f s' % (time.time() - startTime,))

    # Удалить лишние URL-адреса
    links = [href for href in hrefList if 'www.xnxx' in href]
    # Выключить браузер
    # browser.close()
    return links


def downloadVideos(url):
    browser.get(url)
    downloadBtn = browser.find_element_by_xpath("//img[@title='Download']")
    downloadBtn.click()
    time.sleep(1)
    dangerBtn = browser.find_element_by_xpath("//a[@class='text-danger']")
    dangerBtn.click()
    time.sleep(1)
    try:
        emailInput = browser.find_element_by_xpath("//input[@id='signin-form_login']")
        emailInput.send_keys(email)
        passwordInput = browser.find_element_by_xpath("//input[@id='signin-form_password']")
        passwordInput.send_keys(password)
        time.sleep(1)
        login = browser.find_element_by_xpath("//button[@class='btn btn-danger btn-lg']")
        login.click()
    except:
        print('Ошибка, проверьте пароль')
    time.sleep(1)
    downloadBtn = browser.find_element_by_xpath("//img[@title='Download']")
    downloadBtn.click()
    time.sleep(1)
    continue_link = browser.find_element_by_xpath("//*[@id='tabDownload']/p/a[2]")
    continue_link.click()


if __name__ == '__main__':
    from pprint import pprint

    driverpath = "/home/artem/Music/chromedriver"  # Путь к драйверу браузера
    browser = webdriver.Chrome(executable_path=driverpath)
    list_video_href = getListVideoHref()
    pprint(list_video_href)

    email = ''
    password = ''
    downloadVideos(list_video_href[0])

