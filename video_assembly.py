import cv2
import json

with open('config.json', 'r') as json_file:
    config = json.load(json_file)
    fps = config['fps']
    seconds = config['seconds']

frameSize = (1000, 1200)

out = cv2.VideoWriter('output_videoEng.mp4', cv2.VideoWriter_fourcc(*'DIVX'), fps, frameSize)

for n in range(fps*seconds):
    filename = 'imagesEng/filename' + str(n) + '.png'
    img = cv2.imread(filename)
    out.write(img)
out.release()
