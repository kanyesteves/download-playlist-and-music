import os
from pytube import YouTube
# import re

ROOT_OUTPUT_PATH = f"{os.getcwd()}/downloads"  # get dir root os.getcwd()


def download_video(video_id, output_path=f"{ROOT_OUTPUT_PATH}/unknown"):
    try:
        # youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(video_id)
        stream = yt.streams.get_highest_resolution()  # Download in highest resolution

        # If not exist, create the directory
        if not os.path.exists(f"{ROOT_OUTPUT_PATH}/{output_path}"):
            os.makedirs(f"{ROOT_OUTPUT_PATH}/{output_path}")

        if stream:
            stream.download(f"{ROOT_OUTPUT_PATH}/{output_path}")
            print(f" - Baixado com sucesso.")
        else:
            print(f" - Não foi possível encontrar stream para o vídeo")
    except Exception as e:
        print(f" - Erro ao baixar: {str(e)}")


# TODO: future
def download_mp3(video_id, url):
    print(f"Doing...")


# TODO: check to correct filter for URLs:
#  - https://youtube.com/watch?v=ykjtZMKPV1k # Miriam sobre explicação (7,5Mb)
#  - https://youtu.be/S0Wse2hlgpQ?si=hAjD0777TwHVXLVT&t=5 # o JOGO que foi DELETADO do BRASIL (36Mb)
#  - https://youtu.be/9bZkp7q19f0 # Gangnam Style (36Mb)
#  # Playlist Páginas Azuis - 2 videos
#  - https://youtube.com/playlist?list=PLCVTqBt-FMLRyp37E9B5yLj_-QvTPHYcb&si=d1xqE3wZ5srVBIL6
#  # ENTREVISTA COM O EMPRESÁRIO - video 1 da Playlist Páginas Azuis
#  - https://www.youtube.com/watch?v=ZpiKeXnGEEo&list=PLCVTqBt-FMLRyp37E9B5yLj_-QvTPHYcb&index=1&pp=iAQB
'''
def define_uri(url):
    if "watch?v=" in url:
        pattern = r"watch\?v=([^&]+)"
    elif "&" in url:
        pattern = r"(.+?)&"
    else:
        return url

    pattern = r"/([^/?]+)"

    # return video id
    return re.search(pattern, url).group(1)
'''


# needed to handling playlist URL
def file_type(url, type="video"):
    # video_id = define_uri(url)

    download_options = {
        'video': download_video(url, type),
        'mp3': download_mp3
    }

    download_options.get(type)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3", os.path.basename(__file__), "<DOWNLOAD_TYPE> <URL> [QUALITY]")
        sys.exit(1)

    # required quotation marks in URL
    download_type = sys.argv[1]
    url = sys.argv[2]

    # TODO: to resolv, check arg[3]
    # if not sys.argv[3] == None:
    #    quality = sys.argv[3]

    # download_type = [video]/[mp3]
    file_type(url, download_type)
    # file_type(f"{url}", download_type)


'''
    playlist_items = get_playlist_items(api_key, playlist_id, max_results_per_page)

    if playlist_items:
        for item in playlist_items:
            snippet = item['snippet']
            video_id = snippet['resourceId']['videoId']
            video_title = snippet['title']
            print(f"Video ID: {video_id}, Title: {video_title}", end='')
            download_video(video_id, download_type)
    else:
        print("Nenhum vídeo encontrado na playlist.")
'''