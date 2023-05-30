from django.db import models
from rembg import remove
from PIL import Image as PImage
from django.core.files.base import ContentFile
from io import BytesIO
import os


class Image(models.Model):
    img = models.ImageField(upload_to='upload/images/')
    rmbg_img = models.ImageField(upload_to='upload/rmbg_img/', blank=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # output_img = pil_image.convert("RGBA")
        output_path = os.path.splitext(self.img.path)[
            0]+"-bgrm"+os.path.splitext(self.img.path)[1]

        # Open the input image in binary mode
        with open(self.img.path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)

        buffer = BytesIO()
        # output_img = PImage.fromarray(output_img)
        output_img = PImage.open(output_path)
        output_img.save(buffer, format='png')
        val = buffer.getvalue()
        filename = os.path.basename(self.img.path)
        name, _ = filename.split(".")
        name = os.path.split(output_path)[1]
        # self.rmbg_img.save(f"bgrm_{name}.png", ContentFile(val), save=False)
        self.rmbg_img.save(name, ContentFile(val), save=False)
        super().save(*args, **kwargs)
