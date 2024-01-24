import os
from ESPRGAN.espr_gan import ESRGAN_4X
from Multiple.multiple_sr import MultipleSR
from singleton_decorator import singleton


@singleton
class ImageSR:
    def __init__(self, model_name, magnifier):
        my_model = model_name + '_x' + str(magnifier)

        if my_model == 'ESRGAN_x4':
            self.method = ESRGAN_4X()

        elif my_model + '.pb' in os.listdir('super_resolution/Models/SRmodels'):
            self.method = MultipleSR('super_resolution/Models/SRmodels/' + my_model + '.pb')

        else:
            raise NotImplementedError('The mentioned model with this particular magnifying has not been implemented')

    def resolution_enhancement(self, image):
        return self.method.super_res(image)
    