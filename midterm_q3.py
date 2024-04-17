from PIL import Image, ImageOps

# 開啟影像
image = Image.open("carshort_grey.jpg")

# 對影像進行直方圖均衡化處理
enhanced_image = ImageOps.equalize(image)

# 顯示原始影像和增強後的影像
image.show(title="Original Image")
enhanced_image.show(title="Enhanced Image")

# 儲存增強後的影像
enhanced_image.save("enhanced_carshort_grey.jpg")

# 直方圖均衡化是一種影像增強技術，通過重新分佈影像的像素值來增強對比度。
# 它將影像的像素值重新映射到一個更廣的範圍內，以使直方圖更均勻。
# 這樣可以使暗部和亮部的細節更加清晰，從而改善影像的質量。
