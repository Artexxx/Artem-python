"""
YouTubeDownloadMix - скачивает видео из микса с YouTube
"""
from pytube import YouTube
import os
import time
from selenium import webdriver
from tabulate import tabulate


def videoDownload(link, fileLocation):
    try:
        yt = YouTube(link)
        video = yt.streams.filter(progressive=True).all()[0]
        location = os.getcwd()
        if not os.path.exists(location + "/" + fileLocation):
            os.mkdir(fileLocation)
        downloadLocation = location + "/" + fileLocation + '/'
        video.download(downloadLocation)
        print('Download:', link)
    except:
        print('Error: ', link)
        pass


def getVedioList(url):  # choose vedio-List Link
    driverpath = "/home/artem/Music/chromedriver"
    browser = webdriver.Chrome(executable_path=driverpath)
    browser.get(url)
    time.sleep(6)
    # Все элементы для которых определён id:wc-endpoint
    search = browser.find_elements_by_xpath('//*[@id="wc-endpoint"]')
    href_list = [search[i].get_attribute('href') for i in range(len(search))]

    search = browser.find_elements_by_xpath('//*[@id="video-title"]')
    title_list = [search[i].get_attribute('title') for i in range(len(search))]

    search = browser.find_elements_by_xpath('//*[@id="thumbnail-container"]')
    time_list = []
    for i in range(len(search)):
        # Время подгружается динамически, поэтому `span` ещё не существует, увеличьте время и прокрутите страницу
        try:
            time_list.append(search[i].find_element_by_tag_name('span').text)
        except:
            time_list.append('nan-time')
            continue
    browser.close()
    return href_list, title_list, time_list


def youtubeDownloadAll(listUrl, dirName):
    href_list, title_list, time_list = getVedioList(listUrl)
    index = range(len(href_list))

    table = zip(index, time_list, title_list, href_list)
    print(tabulate(table, headers=['Индексы', 'Длительность', 'Название', 'Ссылка']))

    for href in href_list:
        videoDownload(href, dirName)

if __name__ == '__main__':
    sector_gaza = 'https://www.youtube.com/watch?v=Jmw1_t2aMK4&list=RDJmw1_t2aMK4'
    youtubeDownloadAll(sector_gaza, 'SectorGaza')