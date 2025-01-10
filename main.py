import os #Provides functions for interacting with the file system
import argparse #Generates help messages and error messages
from pytube import YouTube #Provides methods to fetch video streams and download from YouTube
from tqdm import tqdm #Library for creating progress bars

#Add a CLI using argparse
def parse_args(): #accepts user input when running the script.
    parser = argparse.ArgumentParser(description="YouTube Download Manager") #Creates an argument parser for the CLI. The description explains what the program does.
    parser.add_argument("--url", required=True, help="YouTube video URL") #Adds a required argument for the YouTube video URL. If the user doesn’t provide it, an error will show.
    parser.add_argument("--output", default="downloads", help="Output folder for downloads") #Adds an optional argument for the output folder where the video will be saved. Defaults to a folder named downloads if not provided.
    parser.add_argument("--resolution", default="720p", help="Desired video resolution") #Adds an optional argument to specify the video resolution (e.g., 720p). Defaults to 720p if not provided.
    return parser.parse_args() #Processes the command-line arguments and returns them for use in the program.

#Check folder existence and create it if needed
def ensure_output_folder(path): #Checks if output folder exists. If it doesn’t, the function creates it.
    if not os.path.exists(path): #Checks if the folder already exists.
        os.makedirs(path) #Creates the folder if it doesn’t exist.



    

