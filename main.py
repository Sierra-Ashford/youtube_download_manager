import os #Provides functions for interacting with the file system (checking if a folder exists, creating folders)
import argparse #Allow users to specify the video URL, output folder, and resolution through the command line
from pytubefix import YouTube #Fetches video streams and downloads from YouTube
from tqdm import tqdm #Library for creating progress bars

#Add a CLI using argparse
def parse_args(): #accepts user input and define what arguments (inputs) the program can accept.
    parser = argparse.ArgumentParser(description="YouTube Download Manager") #Creates an argument parser for the CLI. The description explains what the program does.
    parser.add_argument("--url", required=True, help="YouTube video URL") #Adds a required input for the YouTube video URL. If the user doesn’t provide it, an error will show.
    parser.add_argument("--output", default="downloads", help="Output folder for downloads") #Lets user specify where the downloaded video will be stored. Adds an optional argument for the output folder where the video will be saved. Defaults to a folder named downloads if not provided.
    parser.add_argument("--resolution", default="720p", help="Desired video resolution") #Allows users to control the quality of the downloaded video. Adds an optional argument to specify the video resolution (e.g., 720p). Defaults to 720p if not provided.
    return parser.parse_args() #Processes the inputs and makes them usable in the rest of the program

#Check folder existence and create it if needed
def ensure_output_folder(path): #Checks if output folder exists. If it doesn’t, the function creates it.
    if not os.path.exists(path): #Checks if the folder already exists.
        os.makedirs(path) #Creates the folder if it doesn’t exist.

#Download a video with pytube
def download_video(url, output_folder, resolution): #YouTube(url): Creates a YouTube object for the provided URL, allowing access to video details and streams
    try:
        print(f"Fetching video for {url}...") #Tries to fetch the YouTube video using the URL
        yt = YouTube(url) #Creates an object representing the video

        #Select the stream matching the resolution
        stream = yt.streams.filter(res=resolution, progressive=True).first() #Filters the available streams to find one matching the desired resolution. progressive=True ensures the stream has both video and audio
        if not stream:
            print(f"Resolution {resolution} not available. Downloading the best available resolution.")
            stream = yt.streams.get_highest_resolution() #If the desired resolution isn’t available, this method selects the highest quality available.

        # Download the video
        print(f"Downloading '{yt.title}'...")  #Print message about the download starting
        stream.download(output_folder)  # Downloads the video to the specified folder.
        print(f"Download complete. File saved to: {output_folder}") #Informs user the download is complete
    except Exception as e:  # Handles errors during the video fetching or downloading process
        print(f"An error occurred: {e}")
        

def main(): #Orchestrates the flow of the program
    args = parse_args() #Calls parse_args() to get the user inputs from the command line
    ensure_output_folder(args.output) #Checks if the output folder exists and creates one if needed
    download_video(args.url, args.output, args.resolution) #Calls the download_video() function with the user inputs to fetch and download the video

if __name__ == "__main__": #Ensures the main() function runs only if the script is executed directly
    main()


