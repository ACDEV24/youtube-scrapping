import urllib3
import xlsxwriter
import json
from dateutil import parser

http = urllib3.PoolManager()


def getTopComments(videos, filePath):
    counter = 0
    row = 0
    column = 0

    workbook = xlsxwriter.Workbook(f'{filePath}-Comentarios.xlsx')
    worksheet = workbook.add_worksheet()

    for video in videos:
        try:

            baseUrl = 'https://www.googleapis.com/youtube/v3/commentThreads'
            apiKey = 'AIzaSyCd6enxNAQhq-W_s3pzE-F-TpQFg4pjZ0s'
            parts = 'snippet'
            textFormat = 'plainText'
            maxResults = 100
            videoId = video['url'].replace(
                'https://www.youtube.com/watch?v=',
                ''
            )

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

        items = videoComments['items'] if 'items' in videoComments else []

        worksheet.write(row, column, f'Top: {counter + 1}')
        column += 1

        worksheet.write(row, column, f"Titulo: {video['title']}")
        column += 1

        worksheet.write(row, column, f"Numero de vistas: {video['views']}")
        column += 1

        worksheet.write(row, column, f"URL: {video['url']}")
        column += 1

        row += 1
        column = 0

        if(len(items) == 0):
            worksheet.write(row, 0, 'No tiene comentarios')

        row += 1

        worksheet.write(row, column, '')

        for item in items:
            try:
                if(item['snippet'] == None): return
                if(item['snippet']['topLevelComment'] == None): return
                if(item['snippet']['topLevelComment']['snippet'] == None): return

                snippet = item['snippet']['topLevelComment']['snippet']

                author = snippet['authorDisplayName'] if 'authorDisplayName' in snippet else ''
                text = snippet['textOriginal'] if 'textOriginal' in snippet else ''
                likes = snippet['likeCount'] if 'likeCount' in snippet else ''

                publishedAt = parser.parse(snippet['publishedAt'] if 'publishedAt' in snippet else 'Dic 31 2000 12:00AM')

                if(len(str(publishedAt)) > 0):
                    publishedAt = publishedAt.strftime("%d/%m/%Y")

                worksheet.write(row, column, f'Author: {author}')
                column += 1

                worksheet.write(row, column, f'Comentario: {text}')
                column += 1

                worksheet.write(row, column, f'Numero de likes: {likes}')
                column += 1

                worksheet.write(
                    row,
                    column,
                    f'Fecha de publicacion: {publishedAt}'
                )
                column += 1

                row += 1
                column = 0
            except Exception as e:
                print(f'FAILED CREATING ROW {e}')

        counter += 1
        row += 1
    workbook.close()
