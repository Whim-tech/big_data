

# from PIL import Image
# from numpy import asarray, save
# import numpy as np
# image = Image.open('example.png')
# # summarize some details about the image
# format = image.format
# width = image.size[0]
# height = image.size[1]
# mode = image.mode
# print(image.format)
# print(image.size)
# print(image.mode)
# data = asarray(image)
# print(data.shape)
# save(f"{mode}-{width}x{height}-{format}-example.raw", data)
# read_data = np.load(f"./{mode}-{width}x{height}-{format}-example.raw.npy", mmap_mode="r")
# new_image = Image.fromarray(data.astype('uint8'), 'RGBA')
# print(new_image.format)
# print(new_image.size)
# print(new_image.mode)
# print(read_data.shape)
# print("result:")
# print(np.all(read_data == data))
# print(image == new_image)
# new_image.save("test.png")

import cv2

img = cv2.imread('example.png')
denoised_img = cv2.fastNlMeansDenoising(\
    img, # source image
    None, 
    10, 
    10,
      7)

cv2.imshow('Denoised Image', denoised_img)
cv2.waitKey(0)