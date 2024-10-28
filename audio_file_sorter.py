import os
import shutil
import pygame
import time

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    # Initialize pygame mixer once at the start
    pygame.mixer.init()

    # Set the base folder where the audio files and subfolders are located
    base_folder = os.path.dirname(os.path.abspath(__file__))

    # List all folders in the base folder (for categorizing audio files)
    folders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    print("Available folders:")
    for idx, folder in enumerate(folders, start=1):
        print(f"{idx}. {folder}")

    # Get all audio files in the base folder (excluding folders)
    audio_files = [f for f in os.listdir(base_folder) if f.endswith('.mp3') and os.path.isfile(os.path.join(base_folder, f))]

    # Loop through each audio file and process it
    for i in range(len(audio_files)):
        audio_file = audio_files[i]
        audio_path = os.path.join(base_folder, audio_file)
        
        # Play the next audio file, if there is one
        if i < len(audio_files) - 1:
            next_audio_file = audio_files[i + 1]
            next_audio_path = os.path.join(base_folder, next_audio_file)
            play_audio(next_audio_path)

        print(f"\nPlaying: {audio_file}")

        # Display folder options for user selection
        print("\nChoose a folder to move the audio file:")
        for idx, folder in enumerate(folders, start=1):
            print(f"{idx}. {folder}")
        
        # Get a valid user choice for folder selection
        while True:
            try:
                choice = int(input("Enter the number corresponding to the folder: "))
                if 1 <= choice <= len(folders):
                    selected_folder = folders[choice - 1]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Stop the previous audio to allow it to be moved
        pygame.mixer.music.stop()
        time.sleep(0.1)  # Small delay to ensure the file is fully released

        # Move the current audio file to the selected folder
        destination = os.path.join(base_folder, selected_folder, audio_file)
        shutil.move(audio_path, destination)
        print(f"Moved {audio_file} to {selected_folder}")

    # Quit pygame mixer after all files are moved
    pygame.mixer.quit()

if __name__ == "__main__":
    main()

