import time
from telethon import functions
from telethon.sync import TelegramClient
from yandex_music import Client

import config

api_id = config.api_id
api_hash = config.api_hash

client_ya = Client(config.token)
client_ya.init()

queues = client_ya.queues_list()
last_queue = client_ya.queue(queues[0].id)

last_track_id = last_queue.get_current_track()
last_track = last_track_id.fetch_track()

artists = ', '.join(last_track.artists_name())
title = last_track.title
print(f'Сейчас играет: {artists} - {title}')

music_status = f'🎧 Яндекс Музыка | {artists} - {title}'

    
with TelegramClient('anon', api_id, api_hash) as client:
    client(functions.account.UpdateProfileRequest(about=music_status))
print(f"🆗 Установил статус: «{music_status}»")


if __name__ == '__main__':
    print('🚀 Запускаем...')
    while True:
        try:
            time.sleep(5)
            print(music_status)
        except Exception as e:
            print(f'⚡ Ошибка: {str(e)}')