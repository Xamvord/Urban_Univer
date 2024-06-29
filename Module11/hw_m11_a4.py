from PIL import Image, ImageFilter, ImageDraw, ImageFont

image = Image.open('example.jpg')

new_size = (800, 600)
resized_image = image.resize(new_size)

resized_image.save('resized_image.png')
print("Изображение успешно сохранено в новом формате.")

print()
# ------------------------------------------------------------------------------------- #

image = Image.open('example.jpg')

blurred_image = image.filter(ImageFilter.BLUR)

grayscale_image = image.convert('L')

blurred_image.save('blurred_image.jpg')
grayscale_image.save('grayscale_image.jpg')
print("Изображения успешно обработаны и сохранены.")

print()
# ------------------------------------------------------------------------------------- #

image = Image.open('example.jpg')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", 40)

text = "Пример текста"

draw.text((10, 10), text, font=font, fill=(255, 255, 255))

image.save('image_with_text.jpg')
print("Текст успешно добавлен к изображению.")
