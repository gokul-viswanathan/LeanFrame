'''
Script for extracting video frames
Author: Lu Dong
Date: August 14, 2024
'''

import cv2
import os
import glob
from pdb import set_trace as st 


# This preprocessing script is adapted to work with the following data structure:

# Input structure:
# --input_videos_path
#   --word_name
#       --clean_wordname
#          --video_ids

# Output structure:
# --out_video_frames_path
#   --video_ids_folder
#     --frame_ids


def extract_from_clean_folder(source_directory, destination_directory):
    # Get a list of all video files matching the pattern
    video_files = glob.glob(os.path.join(source_directory, '*.mp4'))

    # Create the destination directory if it doesn't exist
    # os.mkdir(destination_directory)
    print(f'we gonna process {len(video_files)} videos')


    for video_path in video_files:
        # Extract the video name (without extension) from the file path
        video_name = os.path.splitext(os.path.basename(video_path))[0]

        # Create a directory for this video under the destination directory
        video_destination_dir = os.path.join(destination_directory, video_name)
        os.makedirs(video_destination_dir, exist_ok=True)
        
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        frame_number = 1

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            # Save the frame in the video's destination directory
            frame_filename = os.path.join(video_destination_dir, f'{frame_number:04d}.jpg')
            cv2.imwrite(frame_filename, frame)
            
            frame_number += 1

        # Release the video capture object
        cap.release()
        print(f'finish extraction of video {video_name}')

    

if __name__ == '__main__':
    
    #TODO modify to your own path
    src =r'WLASL_CleanProject/processed words 1/src/' 
    dest =r'WLASL_CleanProject/processed words 1/output_video_frames/'
    log_file= "WLASL_CleanProject/processed_words_1/video_over_60.txt"

    for word in os.listdir(src):
        # st()
        clean_folder= os.path.join(src, word, 'clean_'+ word)
        extract_from_clean_folder(clean_folder, dest)
        
    print("Frames extraction complete.")


    # Go through each folder and take notes for frames over 60
    with open(log_file, 'w') as log_file:
        for video_id in os.listdir(dest):
            frame_length= len(os.listdir(os.path.join(dest,video_id)))
            if frame_length > 60:
                log_file.write(f'video {video_id}, frame length is {frame_length}\n')

    # Manually remove the beginning and end frames, ensuring the total length does not exceed 60 frames.
      #TODO 


