from PIL import Image
import os

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.LANCZOS)
        img.save(output_path)

image_folder = 'static/images/'
output_folder = 'static/images/'

# Размеры изображений
new_size = (200, 200)  # Или (200, 200)

# Список изображений для изменения размера
images = ['python.png', 'flask.png', 'bootstrap.png']

for image_name in images:
    input_path = os.path.join(image_folder, image_name)
    output_path = os.path.join(output_folder, image_name)
    resize_image(input_path, output_path, new_size)

print("Изменение размера изображений завершено.")
