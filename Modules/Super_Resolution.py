import os
from ESPRGAN.espr_gan import ESRGAN_4X
from singleton_decorator import singleton
from Diffusion.DiffSR import DiffSuperRes
from GFPGAN.inference_gfpgan import GFPGAN
from Multiple.multiple_sr import MultipleSR


@singleton
class ImageSR:
    def __init__(self, model_name, magnifier):
        my_model = model_name + '_x' + str(magnifier)

        if my_model == 'ESRGAN_x4':
            self.method = ESRGAN_4X()

        elif my_model + '.pb' in os.listdir('../Models/SRmodels'):
            self.method = MultipleSR('../Models/SRmodels/' + my_model + '.pb')
        
        elif model_name == 'GFPGAN':
            self.method = GFPGAN()

        elif model_name == 'StableDiffusion':
            self.method = DiffSuperRes()

        else:
            raise NotImplementedError('The mentioned model with this particular magnifying has not been implemented')

    def resolution_enhancement(self, image, prompt='High quality image with details'):
        if self.model_name == 'StableDiffusion':
            return self.method.super_res(image, prompt)
        else:
            return self.method.super_res(image)
    