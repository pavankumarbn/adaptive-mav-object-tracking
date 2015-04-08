#!/usr/bin/env python2.7

""" Extracts Law's mask features from the drone.
"""

import numpy as np
import cv2


class LawsMask(object):
    """ Law's Mask features.
    """
    def __init__(self):
        # Create the initial laws mask vectors.
        L3 = np.transpose(np.array([1, 2, 1]))
        E3 = np.transpose(np.array([-1, 0, 1]))
        S3 = np.transpose(np.array([-1, 2, -1]))

        L5 = np.transpose(np.array([1, 4, 6, 4, 1]))
        E5 = np.transpose(np.array([-1, -2, 0, 1]))
        S5 = np.transpose(np.array([-1, 0, 2, 0, 1]))

        self.LL3 = np.convolve(L3, np.transpose(L3))
        self.LE3 = np.convolve(L3, np.transpose(E3))
        self.LS3 = np.convolve(L3, np.transpose(S3))
        self.EE3 = np.convolve(E3, np.transpose(E3))
        self.ES3 = np.convolve(E4, np.transpose(S3))
        self.SS3 = np.convolve(S3, np.transpose(S3))

        self.LL5 = np.convolve(L5, np.transpose(L5))
        self.LE5 = np.convolve(L5, np.transpose(E5))
        self.LS5 = np.convolve(L5, np.transpose(S5))
        self.EE5 = np.convolve(E5, np.transpose(E5))
        self.ES5 = np.convolve(E5, np.transpose(S5))
        self.SS5 = np.convolve(S5, np.transpose(S5))

    def extract(self, image, filter_size=5, convert=False):
        """ Extract Law's texture masks from the image. Make sure the image is
            in the YCrCb color space before calling this function.
        """
        if convert:
            image = cv2.cvtColor(imgCV_RGB2YCrCb)

        # Apply the filter.
        (Y, Cr, Cb) = cv2.split(image)
        if filter_size == 3:
            Y_LL  = cv2.filter2D(Y, -1, self.LL3)
            Cr_LL = cv2.filter2D(Y, -1, self.LL3)
            Cb_LL = cv2.filter2D(Y, -1, self.LL3)
            Y_LE  = cv2.filter2D(Y, -1, self.LE3)
            Y_LS  = cv2.filter2D(Y, -1, self.LS3)
            Y_EE  = cv2.filter2D(Y, -1, self.EE3)
            Y_ES  = cv2.filter2D(Y, -1, self.ES3)
            Y_SS  = cv2.filter2D(Y, -1, self.SS3)
        elif filter_size == 5:
            Y_LL  = cv2.filter2D(Y, -1, self.LL3)
            Cr_LL = cv2.filter2D(Y, -1, self.LL3)
            Cb_LL = cv2.filter2D(Y, -1, self.LL3)
            Y_LE  = cv2.filter2D(Y, -1, self.LE3)
            Y_LS  = cv2.filter2D(Y, -1, self.LS3)
            Y_EE  = cv2.filter2D(Y, -1, self.EE3)
            Y_ES  = cv2.filter2D(Y, -1, self.ES3)
            Y_SS  = cv2.filter2D(Y, -1, self.SS3)

        # Construct the feature vector.
        features = np.array(Y_LL, Cr_LL, Cb_LL, Y_LE, Y_LS, Y_EE, Y_ES, Y_SS)
        return features


def test_laws_mask(object):
    sample_imgs = [None]
    laws_mask = LawsMask()
    laws_mask.extract(sample_imgs[0])

if __name__ == '__main__':
    test_laws_mask()
