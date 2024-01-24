import os
import cv2
from numpy import array as to_array
from singleton_decorator import singleton


@singleton
class MultipleSR:
    def __init__(self, model_adrs):
        self.super_res_model = model_adrs

        self.sr = cv2.dnn_superres.DnnSuperResImpl_create()
        self.sr.readModel(self.super_res_model)

        name = os.path.split(model_adrs)
        underline = name[1].index('_')

        self.model = name[1][:underline].lower()
        self.X = int(name[1][underline+2])

    def super_res(self, image):
        self.sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.sr.setModel(self.model, self.X)
        return self.sr.upsample(to_array(image))
    