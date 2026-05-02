import os
import yt_dlp

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
        'watermark': False
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    urls = read_urls_from_file('urls.txt')
    output_path = 'downloads'
    os.makedirs(output_path, exist_ok=True)
    
    for url in urls:
        download_video(url, output_path)

if __name__ == '__main__':
    main()
