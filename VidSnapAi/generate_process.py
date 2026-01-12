# This file looks for new folders inside user_uploads and converts them to reels
import os
import time
import subprocess
from text_to_audio import text_to_speech_file


BASE_DIR = "user_uploads"


def text_to_audio(folder):
    print("TTA - ", folder)
    desc_path = os.path.join(BASE_DIR, folder, "desc.txt")

    if not os.path.exists(desc_path):
        print(f"Skipping {folder}: desc.txt missing")
        return

    with open(desc_path) as f:
        text = f.read()

    text_to_speech_file(text, folder)


def create_reel(folder):
    command = (
        f"./ffmpeg/ffmpeg -f concat -safe 0 "
        f"-i user_uploads/{folder}/input.txt "
        f"-i user_uploads/{folder}/audio.mp3 "
        f'-vf "scale=1080:1920:force_original_aspect_ratio=decrease,'
        f'pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" '
        f"-c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p "
        f"static/reels/{folder}.mp4"
    )

    subprocess.run(command, shell=True, check=True)
    print("CR - ", folder)


if __name__ == "__main__":
    while True:
        print("Processing queue...")

        with open("done.txt", "r") as f:
            done_folders = [line.strip() for line in f]

        for folder in os.listdir(BASE_DIR):
            folder_path = os.path.join(BASE_DIR, folder)

            if not os.path.isdir(folder_path):
                continue

            if folder in done_folders:
                continue

            text_to_audio(folder)
            create_reel(folder)

            with open("done.txt", "a") as f:
                f.write(folder + "\n")

        time.sleep(4)
