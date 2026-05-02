import os
import time
from instagrapi import Client

INSTAGRAM_USERNAME = "thekryptawndog"
INSTAGRAM_PASSWORD = "yashyashyash"

CAPTION = "✨ Cuties of the day! 🐾💕 Follow for daily cute content! #cute #animation #animatedshorts #cuteanimals #satisfying #viral #reels #trending #foryou #foryoupage"

DOWNLOADS_FOLDER = r"C:\Users\yashp\OneDrive\Desktop\downloads"

def main():
    client = Client()
    client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    
    videos = [os.path.join(DOWNLOADS_FOLDER, f) for f in os.listdir(DOWNLOADS_FOLDER) if f.endswith('.mp4')]
    
    for video in videos:
        print(f"Uploading: {video}")
        client.clip_upload(video, CAPTION)
        print("Uploaded! Waiting 2 hours...")
        time.sleep(1800)

if __name__ == '__main__':
    main()