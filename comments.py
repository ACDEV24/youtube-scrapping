import urllib3
import xlsxwriter
import json
from data import names

http = urllib3.PoolManager()
counter = 0


def getTopComments(videos):
    for v in videos:
        try:
            workbook = xlsxwriter.Workbook(f'files/{names[counter]}-Comentarios.xlsx')
            worksheet = workbook.add_worksheet()

            baseUrl = 'https://www.googleapis.com/youtube/v3/videos'
            apiKey = 'AIzaSyCd6enxNAQhq-W_s3pzE-F-TpQFg4pjZ0s'
            parts = 'snippet,statistics,contentDetails'
            textFormat = 'plainText'
            maxResults = 100
            videoId = v.replace('https://www.youtube.com/watch?v=', '')

            url = '{}?key={}&part={}&videoId={}&textFormat={}&maxResults={}'.format(
                baseUrl,
                apiKey,
                parts,
                videoId,
                textFormat,
                maxResults
            )

            videoComments = http.request('GET', url).data.decode('utf-8')
            videoComments = json.loads(videoComments)

        except Exception as e:
            print(f'FAILED FETCH {e}')

        items = videoComments['items']

        for item in items:
            author = item['authorDisplayName']
            text = item['textOriginal']
            likes = item['likeCount']
            publishedAt = item['publishedAt'].strftime("%d/%m/%Y")

            print(item)
    counter += 1
