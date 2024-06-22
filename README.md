# TikTok Video Downloader using Python and yt-dlp

This repository contains a Python script that allows you to download TikTok videos using the `yt-dlp` library. The script is simple to use and can save videos to a specified directory.

## Features

- Download TikTok videos in the best available format.
- Automatically create a save directory if it does not exist.
- Handle download errors gracefully.

## Prerequisites

- Python 3.x
- `yt-dlp` library

## Installation

1. Install `yt-dlp`:
    ```sh
    pip install yt-dlp
    ```

2. Clone this repository or download the script file.

## Usage

Save the script below to a file, e.g., `download_tiktok.py`.

```python
import yt_dlp
import os

def download_tiktok_video(video_url, save_path='tiktok_videos'):
    # Ensure the save directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
        'format': 'best',
    }

    try:
        # Create a yt-dlp object and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"Video successfully downloaded: {filename}")
    
    except Exception as e:
        print(f"Error downloading video: {str(e)}")

# Example usage
video_url = "https://www.tiktok.com/@zachking/video/6768504823336815877?embed_source=121374463%2C121439635%2C121433650%2C121404358%2C121351166%2C121331973%2C120811592%2C120810756%3Bnull%3Bembed_blank&refer=embed&referer_url=marketing4all.es%2Flistas%2Fvideos-mas-vistos-en-tiktok-2024%2F&referer_video_id=6768504823336815877"
download_tiktok_video(video_url)
