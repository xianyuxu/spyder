from PIL import Image
import random

# 開啟原始影像
original_image = Image.open("baboon.png")

# 設定 ROI 的大小
roi_size = (100, 100)

# 設定擷取 ROI 的數量
num_roi = 10

# 擷取並儲存 ROI
for i in range(num_roi):
    # 生成隨機的 ROI 左上角座標
    x = random.randint(0, original_image.width - roi_size[0])
    y = random.randint(0, original_image.height - roi_size[1])

    # 擷取 ROI
    roi = original_image.crop((x, y, x + roi_size[0], y + roi_size[1]))

    # 儲存 ROI 影像檔案
    roi.save(f"ROI{i+1:02d}.bmp")

    # Optional: 顯示儲存的 ROI 影像
    # roi.show()
