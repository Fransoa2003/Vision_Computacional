import cv2
from moviepy import VideoFileClip
import pygame
videoReal = 'video2.mp4'
videoR = VideoFileClip(videoReal)
audio = videoR.audio
pygame.mixer.init()
audio.write_audiofile('audio.mp3')
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
video = cv2.VideoCapture('video2.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
print(f"Frames por segundo: {fps}")
time = int(500 / fps)
while True:
    ret, frame = video.read()
    if ret == True:
        cv2.namedWindow('Video El Despertar', cv2.WINDOW_NORMAL)
        cv2.imshow('Video El Despertar', frame)
    if not ret:
        break
    cv2.imshow('Video El Despertar', frame)
    if cv2.waitKey(time) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()