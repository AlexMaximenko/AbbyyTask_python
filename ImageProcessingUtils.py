import numpy as np
import os
from pdf2image import convert_from_path
from PIL import Image
import random


def convert_pdf_to_img(filepath, union=False):
    """
    Читает pdf из filepath и возвращает:
    Если union = False: список картинок, где каждая страница pdf-файла - отдельная картинка
    Если union = True: весь pdf-файл одной картинкой
    """

    images = convert_from_path(filepath)
    if not union or len(images) < 2:
        return images

    width = images[0].size[0]
    height = images[0].size[1]
    combined_image = Image.new(mode, (width, height * len(images)))
    for i in range(len(images)):
        combined.paste(images[i], (0, images[0].size[1] * i))
    return combined


def add_noise(img, noise_factor=100):
    """
    Добавляет шум к картинке
    img: PIL Image
    """

    pix = np.asarray(img.convert('RGB'))
    width = pix.shape[0]
    height = pix.shape[1]
    new_pix = np.zeros((width, height, 3))
    for i in range(width):
        for j in range(height):
            rand = random.randint(-noise_factor, noise_factor)
            new_pixel = np.array(pix[i, j]) + rand
            new_pixel = np.maximum(new_pixel, 0)
            new_pixel = np.minimum(new_pixel, 255)
            new_pix[i, j] = new_pixel
    return Image.fromarray(new_pix.astype('uint8'))


def save_imgs_to_tiff(imgs, filepath):
    """
    Сохраняет картинку img в формате  .tiff
    imgs: list of PIL Images
    """
    if len(imgs) > 1:
        imgs[0].save(filepath, 'TIFF', save_all=True, append_images=imgs[1:])
    else:
        imgs[0].save(filepath, 'TIFF')