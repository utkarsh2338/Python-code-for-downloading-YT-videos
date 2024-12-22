import yt_dlp
import os

def download_youtube_video():
    video_url = input("Enter the YouTube video URL: ").strip()
    save_path = input("Enter the directory to save the video (default is current directory): ").strip() or "."

    # Ensure the save path exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    options = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',  # Best quality with audio and video
        'merge_output_format': 'mp4',         # Output format after merging
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
