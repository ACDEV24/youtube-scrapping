from pytube import YouTube
from pytube import Channel

videos = [
    'https://www.youtube.com/channel/UCSRDdJckljibYXTbR_7LgOQ/videos'
]

for video in videos:
    channel_info = Channel(video)

    for url in channel_info.url_generator():
        video_details = YouTube(url)
        views = video_details.views
        title = video_details.title
        author = video_details.author
        publish_date = video_details.publish_date
        duration = video_details.streaming_data["formats"][0]["approxDurationMs"]
        duration = int(duration)

        seconds=(duration/1000)%60
        seconds = int(seconds)
        minutes=(duration/(1000*60))%60
        minutes = int(minutes)
        hours=(duration/(1000*60*60))%24

        duration = "%d:%d:%d" % (hours, minutes, seconds)

        print('---------------------------------------------------------')
        print(f'URL: {url}')
        print(f'Autor: {author}')
        print(f'Titulo: {title}')
        print(f'Numero de visitas: {views}')
        print(f'Duracion: {duration}')
        print(f'Fecha de publicacion: {publish_date}')
        print('---------------------------------------------------------\n')
