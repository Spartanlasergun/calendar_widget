import base64

def create(img):
    with open(img, "rb") as image_file:
        # Read the image file in binary mode
        image_data = image_file.read()
        # Encode the image data as a base64 string
        base64_string = base64.b64encode(image_data).decode("utf-8")

    # write to txt file
    write = open('img.txt', 'w', encoding='utf-8')
    write.write(base64_string)
    write.close()

create('default.gif')