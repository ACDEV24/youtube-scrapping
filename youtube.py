from selenium import webdriver
from bs4 import BeautifulSoup
import urllib3
import json

http = urllib3.PoolManager()

urls = [
    'https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ'
]


def main():
    driver = webdriver.Chrome(
        executable_path=r'/Users/ac/Downloads/chromedriver')
    for url in urls:
        driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a', id='video-title')
        views = soup.findAll(
            'span', class_='style-scope ytd-grid-video-renderer')
        video_urls = soup.findAll('a', id='video-title')
        print('Channel: {}'.format(url))
        i = 0
        j = 0
        print()
        for title in titles:
            videoReference = video_urls[j].get('href')
            baseUrl = 'https://www.googleapis.com/youtube/v3/videos'
            apiKey = 'AIzaSyCd6enxNAQhq-W_s3pzE-F-TpQFg4pjZ0s'
            parts = 'snippet,statistics,contentDetails'

            videoId = videoReference.replace('/watch?v=', '')
            url = '{}?key={}&part={}&id={}'.format(
                baseUrl, apiKey, parts, videoId)

            videoDetails = http.request('GET', url).data.decode('utf-8')
            videoDetails = json.loads(videoDetails)

            publishedAt = videoDetails['items'][0]['snippet']['publishedAt'][:-10]

            duration = videoDetails['items'][0]['contentDetails']['duration'].replace(
                'PT', '')
            duration = duration.replace('H', ' Horas ')
            duration = duration.replace('M', ' Minutos ')
            duration = duration.replace('S', ' Segundos ')

            videoViews = views[i].text

            videoTitle = title.text

            print('---------------------------------------------------------')
            print('Titulo: {}'.format(videoTitle))
            print('Duracion: {}'.format(duration))
            print('Visitas: {}'.format(videoViews))
            print('Fecha de publicacion: {}'.format(publishedAt))
            print('URL: https://www.youtube.com{}'.format(videoReference))
            print('---------------------------------------------------------\n')
            i += 2
            j += 1


main()
