from PIL import Image

# 開啟照片
image = Image.open("over_exposure_grey.jpg")

# 降低亮度
darkened_image = Image.new(image.mode, image.size)
pixels = darkened_image.load()

for i in range(image.size[0]):
    for j in range(image.size[1]):
        # 取得原始像素值
        pixel_value = image.getpixel((i, j))

        # 降低亮度
        new_pixel_value = int(pixel_value * 0.5)

        # 設置新的像素值
        pixels[i, j] = new_pixel_value

# 儲存降低亮度後的照片
darkened_image.save("darkened_over_exposure.jpg")
