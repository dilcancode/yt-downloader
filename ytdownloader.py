from pytubefix import YouTube
from moviepy import AudioFileClip
from InquirerPy import inquirer
import os
import sys

default_path = "YOUR_PATH_HERE"

#audio
def get_audio(url,save_path=default_path):
	try:
		if not os.path.exists(save_path):
			os.mkdir(save_path)
			print(f"{save_path} doesn't exist so we created one!")
		
		
		video = YouTube(url)
		print(f"Downloading...")
		#video info
		print("-"*20+"Video info"+"-"*20)
		print(f"Title : {video.title}\nChannel : {video.author}\nLength : {video.length} sec")
		print("-"*50)

		#download the video
		audio = video.streams.filter(only_audio=True).first()
		download = audio.download(output_path=save_path)

		#convert to audio
		name  = os.path.splitext(download)[0]
		mp3 = name + ".mp3"

		
		audio_file = AudioFileClip(download)
		audio_file.write_audiofile(mp3)
		audio_file.close()

		os.remove(download)
		
	except Exception as e:
		print(f"Error : {e}")



#video 
def get_video(url,save_path=default_path):
	try:
		if not os.path.exists(save_path):
			os.mkdir(save_path)
			print(f"{save_path} doesn't exist so we created one")

		video = YouTube(url)
		print(f"Downloading...")
		print("-"*20+"Video info"+"-"*20)
		print(f"Title : {video.title}\nChannel : {video.author}\nLength : {video.length}")
		print("-"*50)

		resolution = inquirer.select(
			message="Select your resolution.",
			choices=["highest resolution","480p","360p"],
			default="720p").execute()
		
		if resolution == "highest resolution":
			video_file = video.streams.get_highest_resolution()
		
		else:
			video_file = video.streams.get_by_resolution(resolution=resolution)
		
		download = video_file.download(output_path=save_path)	
		print(f"Completed!\nSaved to {save_path}.")

	except Exception as e:
		print(f"Error {e}")	


def main():
    try:
        link = input("Enter the YouTube video link: ").strip()
        if not link:
            print("You must enter a URL!")
            return

        choice = inquirer.select(
            message="Choose download format:",
            choices=["MP3", "MP4", "Exit"],
        ).execute()

        if choice == "MP3":
            get_audio(link)
        elif choice == "MP4":
            get_video(link)
        else:
            print("Exiting...")
            sys.exit(0)

    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(0)

# Run  the  program
if __name__ == "__main__":
    main()
	 




