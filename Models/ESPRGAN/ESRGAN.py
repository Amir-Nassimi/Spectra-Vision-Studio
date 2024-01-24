import tensorflow as tf
import tensorflow_hub as hub
from numpy import array as to_array
from singleton_decorator import singleton


@singleton
class ESRGAN_4X:
    def __init__(self, model_path="https://www.kaggle.com/models/kaggle/esrgan-tf2/frameworks/TensorFlow2/variations/esrgan-tf2/versions/1"):
        self.model = hub.load(model_path)

    def preprocessing(self, img):
        imageSize = (tf.convert_to_tensor(img.shape[:-1]) // 4) * 4
        cropped_image = tf.image.crop_to_bounding_box(img, 0, 0, imageSize[0], imageSize[1])
        return tf.expand_dims(tf.cast(cropped_image, tf.float32), 0)

    def super_res(self, img):
        img = to_array(img)
        new_image = self.model(self.preprocessing(img))
        return tf.squeeze(new_image) / 255.0
