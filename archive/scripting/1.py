from PIL import Image, ImageFilter

print("--------------------------------")
x= Image.open('./images/test_pattern.jpeg')

print(x)
print(x.format)
print(x.size)
print(x.mode)

x_filter = x.filter(ImageFilter.BLUR)
x_filter.save("./images/test_blur.png","png")

print("--------------------------------")
x_filter = x.convert('L')
x_filter.save("./images/gray.png","png")
print(x_filter.format)
print(x_filter.size)
print(x_filter.mode)

x_rotated = x.rotate(90)
x_rotated.save("./images/test_rotate_90.png","png")

print("--------------------------------")

resized = x.resize((200,200))
resized.save("./images/test_resized.png","png")


print("--------------------------------")

y = Image.open('./images/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpeg')

x_axis = 1700
y_axis = 150
crop_box = (x_axis,y_axis,x_axis + 400, y_axis + 400)

crop = y.crop(crop_box)
# crop.show()
crop.save("./images/Botticelli_cropped.png","png")



