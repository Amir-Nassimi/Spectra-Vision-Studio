import argparse
from PIL import Image
from Modules.super_resolution import ImageSR


class SuperResolutionApp:
    def __init__(self, model_name, magnification, image_path):
        self.model_name = model_name
        self.magnification = magnification
        self.image_path = image_path
        self.model_magnification_map = {
            "EDSR": [2, 3, 4],
            "ESPCN": [2, 3, 4],
            "FSRCNN": [2, 3, 4],
            "LapSRN": [2, 4, 8],
            "ESRGAN": [4]
        }

    def validate_model_and_magnification(self):
        if self.model_name in self.model_magnification_map:
            if self.magnification in self.model_magnification_map[self.model_name]:
                return True
        return False

    def run_super_resolution(self):
        if not self.validate_model_and_magnification():
            raise ValueError(f"Magnification factor {self.magnification} is not valid for model {self.model_name}")

        # Initialize the ImageSR class
        my_class = ImageSR(self.model_name, self.magnification)

        # Perform resolution enhancement
        img = Image.open(self.image_path)
        img_hr = my_class.resolution_enhancement(img)
        img_hr.show()


def main():
    parser = argparse.ArgumentParser(description='Image Super-Resolution')
    parser.add_argument('--model_name', type=str, help='Name of the super-resolution model')
    parser.add_argument('--magnification', type=int, help='Magnification factor')
    parser.add_argument('--image_path', type=str, help='Path to the image file')

    args = parser.parse_args()

    app = SuperResolutionApp(args.model_name, args.magnification, args.image_path)
    app.run_super_resolution()

if __name__ == "__main__":
    main()
