#!/usr/bin/python3
import pyyolo
import numpy as np
import sys
from cv2 import imread

darknet_path = './darknet'
datacfg = darknet_path + 'cfg/nfpa.data'
cfgfile = darknet_path + 'cfg/yolov2.cfg'
weightfile = '../yolo-nfpa_1500.weights'
files = [ darknet_path + '/data/fd_01.jpg',
          darknet_path + '/data/fd_02.jpg',
          darknet_path + '/data/fd_03.jpg' ]

thresh = 0.24
hier_thresh = 0.5

pyyolo.init(darknet_path, datacfg, cfgfile, weightfile)

# camera
print('----- test python API using a file')
i = 0
while i < len(files):
    filename = files[i]
    print(filename)
	# ret_val, img = cam.read()
    img = imread(filename)
    img = img.transpose(2,0,1)
    c, h, w = img.shape[0], img.shape[1], img.shape[2]
    # print w, h, c
    data = img.ravel()/255.0
    data = np.ascontiguousarray(data, dtype=np.float32)
    outputs = pyyolo.detect(w, h, c, data, thresh, hier_thresh)
    for output in outputs:
        print(output)
    i += 1


# free model
pyyolo.cleanup()

