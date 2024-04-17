from PIL import Image, ImageFilter

# 開啟影像
image = Image.open("over_exposure_grey.jpg")

# 使用邊緣增強濾鏡增強影像
enhanced_image = image.filter(ImageFilter.EDGE_ENHANCE)

# 顯示原始影像和增強後的影像
image.show(title="Original Image")
enhanced_image.show(title="Enhanced Image")

# 儲存增強後的影像
enhanced_image.save("edge_enhanced_over_exposure_grey.jpg")

# 邊緣增強是一種影像增強技術，它通過增強影像中的邊緣特徵來提高影像的對比度和清晰度。
# 使用邊緣增強濾鏡可以使影像中的邊緣更加鮮明，從而使物體的輪廓更加清晰。
