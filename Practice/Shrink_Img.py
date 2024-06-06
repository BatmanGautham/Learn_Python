from PIL import Image as I

img = I.open("colorful flowers.jpg")

S_factor = 2
new_Width = img.width//S_factor
new_height = img.height//S_factor

Shrink_img = img.resize((new_Width,new_height))

Shrink_img.save("Shrink_image.jpg")

Shrink_img.show()