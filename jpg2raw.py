import numpy as np
import cv2
import glob
import os


def jpg2raw():
    imglist = glob.glob('*.jpg')
    if len(imglist) > 0:
        os.makedirs('./RawFile', exist_ok=True)
        print('Start!')
        for img in imglist:
            img_data = cv2.imdecode(np.fromfile(img, dtype='uint8'), -1)
            img_array = np.asarray(img_data)
            np.ndarray.tofile(img_array, './RawFile/%s-raw.raw' % os.path.basename(img)[:-4])
    else:
        print('No jpg file...\n')


if __name__ == '__main__':
    jpg2raw()
    bye = input('Press enter to exit.\n')


