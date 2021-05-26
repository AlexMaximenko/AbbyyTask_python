import ImageProcessingUtils as ipu

filepath = './abbyy_test.pdf'
respath = './abbyy_results.tif'

imgs = ipu.convert_pdf_to_img(filepath)

for i in range(len(imgs)):
    imgs[i] = ipu.add_noise(imgs[i])

ipu.save_imgs_to_tiff(imgs, respath)