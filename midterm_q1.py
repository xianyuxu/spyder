from PIL import Image

# 設定影像大小
image_size = 512

# 設定每個格子的大小
grid_size = image_size // 8

# 建立新的影像物件
image = Image.new('L', (image_size, image_size), color=255)  # 'L' 代表灰階影像，color=255 是白色

# 在每個格子上交替設定灰階值
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            # 如果 i+j 是偶數，則設定該格為黑色(灰階值 0)
            box = (j * grid_size, i * grid_size, (j + 1) * grid_size, (i + 1) * grid_size)
            image.paste(0, box)
        else:
            # 如果 i+j 是奇數，則保持為白色(灰階值 255)
            pass

# 儲存影像檔案
image.save("output.bmp")
