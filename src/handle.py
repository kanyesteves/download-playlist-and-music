#
# Author: willyamcts
# Description: list all videos/shorts from any playlist (using API key) and download (without API key) to the directory with the playlist name
#

import os
import requests
from pytube import YouTube

def download_video(video_id, output_path="."):
    try:
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()  # Baixa a versão com a maior resolução disponível

        # Verifica se o diretório de saída existe, senão cria
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        if stream:
            stream.download(output_path)
            print(f" - Baixado com sucesso.")
        else:
            print(f" - Não foi possível encontrar stream para o vídeo")
    except Exception as e:
        print(f" - Erro ao baixar o vídeo: {str(e)}")

def get_playlist_items(api_key, playlist_id, max_results=50):
    base_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    params = {
        'part': 'snippet',
        'playlistId': playlist_id,
        'maxResults': max_results,
        'key': api_key,
    }

    playlist_items = []

    next_page_token = None
    while True:
        if next_page_token:
            params['pageToken'] = next_page_token

        response = requests.get(base_url, params=params)
        data = response.json()

        if 'items' in data:
            playlist_items.extend(data['items'])

        next_page_token = data.get('nextPageToken')

        if not next_page_token:
            break

    return playlist_items

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3", os.path.basename(__file__), "<API_KEY> <PLAYLIST_ID>")
        sys.exit(1)

    api_key = sys.argv[1]
    playlist_id = sys.argv[2]

    # Quantidade máxima de resultados por página
    max_results_per_page = 200

    playlist_items = get_playlist_items(api_key, playlist_id, max_results_per_page)

    if playlist_items:
        for item in playlist_items:
            snippet = item['snippet']
            video_id = snippet['resourceId']['videoId']
            video_title = snippet['title']
            print(f"Video ID: {video_id}, Title: {video_title}", end='')
            download_video(video_id, playlist_id)
    else:
        print("Nenhum vídeo encontrado na playlist.")
