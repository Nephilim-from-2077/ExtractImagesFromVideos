import cv2
import os

# Create a folder named "frames" if it doesn't exist
if not os.path.exists("frames"):
    os.makedirs("frames")

# Open the video file
cap = cv2.VideoCapture('video56.MOV')

# Check if the video file was opened successfully
if not cap.isOpened():
    print('Error opening video file')
    exit()

# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Get the frames per second (fps) of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Calculate the time interval between frames in seconds
time_interval = 1.0

# Calculate the number of frames to skip between captures
frames_to_skip = int(time_interval * fps)

# Loop through each frame and save it as an image file every 2 seconds
frame_counter = 0
for i in range(total_frames):
    # Read the next frame
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print('Error reading frame')
        break

    # Increment the frame counter
    frame_counter += 1

    # Save the frame as an image file every n frames
    if frame_counter % frames_to_skip == 0:
        cv2.imwrite(f'frames/frame_{i}.jpg', frame)

# Release the video file and close the window
cap.release()
cv2.destroyAllWindows()
