# install pillow
# import pillow
# open up the image we want to resize using python
# print the current size of that image
# specify the size we wanna change it to
# save the new resized image

from PIL import Image

img_name = input("Enter Image Name: ")
image = Image.open(img_name)

print(f"Current Size: {image.size}")

def resize_image(width, height):


    resized_image = image.resize((width, height))

    resized_image.save('resized1.png')

    print(f"New Size: {resized_image.size}")


width = int(input('Enter Width: '))
height = int(input('Enter Height: '))
resize_image(width, height)