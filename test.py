from PIL import Image

image = Image.open('images/full.png')
image = image.crop((474, 208, 1380, 688))
image.save('images/test.png')