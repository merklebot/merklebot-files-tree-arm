import os

print("Start recording audio")
sample_name = "aaaa.wav"
cmd = f'arecord -vv --format=cd --device={os.environ["AUDIO_INPUT_DEVICE"]} -r 48000 --duration=10 -c 1 {sample_name}'
print(cmd)
os.system(cmd)
print("Playing sound")
os.system(f"ffplay -nodisp -autoexit -loglevel quiet {sample_name}")

# Capture image
import cv2
camera_capture = cv2.VideoCapture(0)
rv, image = camera_capture.read()
print(f"Image Dimensions: {image.shape}")
camera_capture.release()
