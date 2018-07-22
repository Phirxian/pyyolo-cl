#!/usr/bin/python3
import pyyolo
import numpy as np
import glob
import sys
import cv2
import os

from tqdm import tqdm

darknet_path = './darknet'
datacfg = 'cfg/coco.data'
cfgfile = 'cfg/yolov3.cfg'
weightfile = './backup/goat/goat_200.weights'
thresh = 0.001
hier_thresh = 0.0

os.chdir(darknet_path)
pyyolo.init(darknet_path, datacfg, cfgfile, weightfile)

folder = '/root/Documents/tool/pyyolo/darknet/data/goat/images/'
folder = '/run/media/root/Ascomycete/Stage/pasture/set-97/camera-3/frames/'
#folder = '/run/media/root/Ascomycete/Stage/03-skylan-shot/150517/g2/'
#folder = '/root/Documents/school/toulouse/m2.5/stage/02-hough-goat-detection/hough/set/'

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
files = glob.glob(folder + '*.jpg')[4000:]

for filename in files:
    # ret_val, img = cam.read()
    img = cv2.imread(filename)
    img = img.transpose(2,0,1)
    c, h, w = img.shape[0], img.shape[1], img.shape[2]
    # print w, h, c 
    data = img.ravel()/255.0
    data = np.ascontiguousarray(data, dtype=np.float32)
    outputs = pyyolo.detect(w, h, c, data, thresh, hier_thresh)	

    img = cv2.imread(filename)
    for output in tqdm(outputs):
    
        if output['right']-output['left'] > 100:
            continue
    
        if output['top']-output['bottom'] > 100:
            continue
            
        print((output['left'], output['top'], output['right'], output['bottom']))
        cv2.rectangle(
            img,
            (output['left'], output['top']),
            (output['right'], output['bottom']),
            (255,0,0), 4
        )
    pass
    
    cv2.imshow("Original", img)
    k = cv2.waitKey() & 0xff
    
    if k == 27:
        break
pass

# free model
pyyolo.cleanup()
