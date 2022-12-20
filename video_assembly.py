import cv2
import json

with open('config.json', 'r') as json_file:
    config = json.load(json_file)
    fps = config['fps']
    seconds = config['seconds']

frameSize = (2000, 2400)

out = cv2.VideoWriter('video/output_videoEngEU.mp4', cv2.VideoWriter_fourcc(*'MP4V'), fps, frameSize)

for n in range(fps*seconds):
    filename = 'images/touristEU/imagesEng/shot' + str(n) + '.png'
    img = cv2.imread(filename)
    out.write(img)
out.release()
