""" VL_DEMO_SIFT_EDGE  Demo: SIFT: edge threshold """

import numpy as np
import matplotlib.pyplot as plt
import vlfeat
from vlfeat.plotop.vl_plotframe import vl_plotframe

if __name__ == '__main__':

    I = np.zeros([100, 500])
    for i in 10 * (1 + np.arange(9)):
        d = np.round(i / 3.0)
        I[50 - d - 1:50 + d - 1, i * 5 - 1] = 1

    I = np.array(I, 'f', order='F')
    I = 2 * np.pi * 8 ** 2 * vlfeat.vl_imsmooth(I, 8)
    I *= 255

    I = np.array(I, 'f', order='F')

    print 'sift_edge_0'

    ter = [3.5, 5, 7.5, 10]
    for te in ter:
        f, d = vlfeat.vl_sift(I, peak_thresh=0.0, edge_thresh=te)

        plt.figure()
        plt.gray()
        plt.imshow(I)
        vl_plotframe(f, color='k', linewidth=3)
        vl_plotframe(f, color='y', linewidth=2)

    plt.show()
