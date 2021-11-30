from PIL import Image, ImageDraw


def draw(s):
    img = Image.new('RGB', (1280, 720), color=(0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((0, 0), s, fill=(255, 255, 255))
    img.save("temp.jpg")
