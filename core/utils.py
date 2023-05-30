from rembg import remove
from PIL import Image as PImage
from django.core.files.base import ContentFile
from io import BytesIO


def remove_bg(image):
    # Open the input image in binary mode
    input = image.read()
    output = remove(input)

    return output
    # buffer = BytesIO()
    # # output_img = PImage.fromarray(output_img)
    # output_img = PImage.open(output_path)
    # output_img.save(buffer, format='png')
    # val = buffer.getvalue()
    # filename = os.path.basename(self.img.path)
    # name, _ = filename.split(".")
    # name = os.path.split(output_path)[1]
    # # self.rmbg_img.save(f"bgrm_{name}.png", ContentFile(val), save=False)
    # self.rmbg_img.save(name, ContentFile(val), save=False)
