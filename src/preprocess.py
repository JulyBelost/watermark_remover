import os
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt


def read_images(raw_dir):
    files = os.listdir(raw_dir)
    images_raw = {}

    for file in files:
        path = (os.sep.join([os.path.abspath(raw_dir), file]))
        img = cv2.imread(path)
        if img is not None:
            images_raw[file] = img
        else:
            print("%s not found." % (file))

    return images_raw


def preprocess(images_raw, size):
    images = {}

    show = True
    for file, img in images_raw.items():
        m, n, p = img.shape
        m_t, n_t = (size - m) // 2, (size - n) // 2
        final_img = np.pad(img, ((m_t, size - m - m_t), (n_t, size - n - n_t), (0, 0)), mode='mean')
        if show:
            img_res = final_img[:, :, ::-1]
            plt.figure(dpi=600)
            plt.imshow(img_res)
            plt.xticks([]), plt.yticks([])
            plt.show()
            show = False
        images[file] = final_img

    return images


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Format : %s <foldername>" % (sys.argv[0]))
    else:
        preprocess(sys.argv[1])
