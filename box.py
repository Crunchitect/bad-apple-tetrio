import cv2
import numpy as np
import glob

frameSize = (1920, 1080)

out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 36, frameSize)

for filename in glob.glob('output/*.png'):
    print(filename)
    img = cv2.imread(filename)
    out.write(img)

out.release()