import yt_dlp
import os
import re

def download_tiktok_video(video_url, save_path='tiktok_videos'):
    # Ensure the save directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Validate the TikTok URL
    if not re.match(r'https?://(www\.)?tiktok\.com/.*', video_url):
        print("Invalid TikTok URL.")
        return

    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s-%(id)s.%(ext)s'),  # Save with title and ID for better identification
        'format': 'best',  # Download the best available quality
        'noplaylist': True,  # Avoid downloading playlists
        'quiet': False,  # Show download progress
        'progress_hooks': [progress_hook],  # Hook for progress reporting
    }

    try:
        # Create a yt-dlp object and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"\nVideo successfully downloaded: {filename}")
    
    except yt_dlp.utils.DownloadError as e:
        print(f"Error downloading video: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} at {d['_speed_str']} ETA: {d['_eta_str']}", end='\r')
    elif d['status'] == 'finished':
        print("\nDownload completed, finalizing...")

# Example usage
video_url = "https://www.tiktok.com/@zachking/video/6768504823336815877"
download_tiktok_video(video_url)
