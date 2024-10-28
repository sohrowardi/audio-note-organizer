import os
import shutil
import pygame
import time
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_pygame():
    pygame.mixer.init()

def list_folders(base_folder):
    folders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    return folders

def list_audio_files(base_folder, extension='.mp3'):
    audio_files = [f for f in os.listdir(base_folder) if f.endswith(extension) and os.path.isfile(os.path.join(base_folder, f))]
    return audio_files

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()
    time.sleep(0.5)  # Increased delay to ensure file release

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        logging.info(f"Moved {source} to {destination}")
    except Exception as e:
        logging.error(f"Error moving file: {e}")

def main():
    initialize_pygame()
    
    base_folder = os.path.dirname(os.path.abspath(__file__))
    folders = list_folders(base_folder)
    
    print("Available folders:")
    for idx, folder in enumerate(folders, start=1):
        print(f"{idx}. {folder}")
    
    audio_files = list_audio_files(base_folder)
    
    if not audio_files:
        print("No audio files found.")
        return

    i = 0
    while i < len(audio_files):
        audio_file = audio_files[i]
        audio_path = os.path.join(base_folder, audio_file)

        play_audio(audio_path)
        
        print(f"\nPlaying: {audio_file}")

        print("\nChoose a folder to move the audio file or press 0 to skip:")
        for idx, folder in enumerate(folders, start=1):
            print(f"{idx}. {folder}")
        
        while True:
            try:
                choice = int(input("Enter the number corresponding to the folder (or 0 to skip): "))
                if choice == 0:
                    print("Skipped the audio file.")
                    i += 1
                    break
                elif 1 <= choice <= len(folders):
                    selected_folder = folders[choice - 1]
                    stop_audio()  # Ensure audio is stopped before moving
                    destination = os.path.join(base_folder, selected_folder, audio_file)
                    move_file(audio_path, destination)
                    i += 1
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
    print("No more audio files in the folder.")
    pygame.mixer.quit()

if __name__ == "__main__": 
    main()
