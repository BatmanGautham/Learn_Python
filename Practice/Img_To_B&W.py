from PIL import Image as I

image = I.open("colorful flowers.jpg")

greyImg = image.convert('L')

greyImg.save('greyscale_image.jpg')

greyImg.show()
