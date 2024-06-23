 # TikTok Video Downloader using Python and yt-dlp

![TikTok Cover](https://brandemia.org/contenido/subidas/2023/01/1-2017-1024x576.jpg](https://cdn.pixabay.com/photo/2021/01/30/06/42/tiktok-5962992_960_720.png)

This repository contains a Python script that allows you to download TikTok videos using the `yt-dlp` library. The script is simple to use and can save videos to a specified directory.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=green&labelColor=green)
![Git](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Telegram](https://img.shields.io/badge/telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

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
```

## Running the Script

1. Save the script to a file, e.g., `download_tiktok.py`.
2. Run the script:
    ```sh
    python download_tiktok.py
    ```
3. The script will download the specified TikTok video and save it in the `tiktok_videos` directory (or any directory you specify).

## Parameters

- `video_url`: URL of the TikTok video.
- `save_path`: Directory where the video will be saved (default: `'tiktok_videos'`).

## Example

```python
video_url = "https://www.tiktok.com/@zachking/video/6768504823336815877?embed_source=121374463%2C121439635%2C121433650%2C121404358%2C121351166%2C121331973%2C120811592%2C120810756%3Bnull%3Bembed_blank&refer=embed&referer_url=marketing4all.es%2Flistas%2Fvideos-mas-vistos-en-tiktok-2024%2F&referer_video_id=6768504823336815877"
download_tiktok_video(video_url)
```

This example downloads the specified TikTok video and saves it in the `tiktok_videos` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



