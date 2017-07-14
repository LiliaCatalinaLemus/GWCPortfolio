from PIL import Image
im = Image.open("harry.jpg")
im.show()
new_image = Image.new(im.mode, im.size)
new_image.save("output.jpg", "jpeg")

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)


# Import image.
image_list = im.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

for pixels in image_list:
    R, B, G = pixels
    if int(R) + int(B) + int(G) <182:
        recolored.append(darkBlue)
    elif int(R) + int(B) + int(G) <364:
        recolored.append(red)
    elif int(R) + int(B) + int(G) <546 :
        recolored.append(lightBlue)
    else:
        recolored.append(yellow)



# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", im.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
