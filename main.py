from pytube import YouTube
from pytube import Channel
import xlsxwriter

videos = [
    # 'https://www.youtube.com/channel/UCSRDdJckljibYXTbR_7LgOQ/videos' # TEST
    'https://www.youtube.com/c/Yanbal-CanalOficial/videos',
    'https://www.youtube.com/user/avoncolombia/videos',
    'https://www.youtube.com/c/MaybellineNewYorkColombia/videos',
    'https://www.youtube.com/c/EsikaBelcorp/videos',
    'https://www.youtube.com/user/NaturaCoOficial/videos',
    'https://www.youtube.com/c/MASGLOOficial/videos',
    'https://www.youtube.com/c/VogueCosm%C3%A9ticosColombiaes/videos ',
    'https://www.youtube.com/user/cosmeticosJolie/videos',
]

titles = ['Titulo', 'Numero de visitas', 'Duracion',
        'Año de publicación', 'Fecha de publicacion', 'Author', 'URL']
names = ['Yanbal', 'Avon', 'Maybelline', 'Esika',
         'Natura', 'Masglo', 'Vogue', 'Jolie de vogue']
counter = 0

for video in videos:
    channel_info = Channel(video)

    workbook = xlsxwriter.Workbook(f'files/{names[counter]}.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    column = 0

    for title in titles:
        worksheet.write(0, column, title)
        column += 1

    column = 0

    for url in channel_info.url_generator():
        video_details = YouTube(url)
        views = video_details.views
        title = video_details.title
        author = video_details.author
        publish_date = video_details.publish_date
        publish_year = publish_date.year
        publish_date = publish_date.strftime("%d/%m/%Y")
        duration = video_details.streaming_data["formats"][0]["approxDurationMs"]
        duration = int(duration)

        seconds = (duration/1000) % 60
        seconds = int(seconds)
        minutes = (duration/(1000*60)) % 60
        minutes = int(minutes)
        hours = (duration/(1000*60*60)) % 24

        duration = "%d:%d:%d" % (hours, minutes, seconds)

        print('---------------------------------------------------------')
        print(f'Titulo: {title}')
        worksheet.write(row, column, title)
        column += 1
        print(f'Numero de visitas: {views}')
        worksheet.write(row, column, views)
        column += 1
        print(f'Duracion: {duration}')
        worksheet.write(row, column, duration)
        column += 1
        print(f'Año de publicacion: {publish_year}')
        worksheet.write(row, column, publish_year)
        column += 1
        print(f'Fecha de publicacion: {publish_date}')
        worksheet.write(row, column, publish_date)
        column += 1
        print(f'Autor: {author}')
        worksheet.write(row, column, author)
        column += 1
        print(f'URL: {url}')
        worksheet.write(row, column, url)
        column += 1
        print('---------------------------------------------------------\n')
        row += 1
        column = 0
    counter += 1
    workbook.close()
