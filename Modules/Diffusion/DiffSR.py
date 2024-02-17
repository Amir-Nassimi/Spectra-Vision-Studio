import torch
from diffusers import StableDiffusionUpscalePipeline


class DiffSuperRes:
    def __init__(self, model_path="stabilityai/stable-diffusion-x4-upscaler"):
        self.pipeline = StableDiffusionUpscalePipeline.from_pretrained(model_path, revision="fp16", torch_dtype=torch.float32)

    def super_res(self, img, prompt):
        return self.pipeline(prompt=prompt, image=img).images[0]