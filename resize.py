import os
from PIL import Image
from resizeimage import resizeimage

try:
    directory_raw = '/app/raw-images'
    directory_resized = '/app/raw-images/1024px'

    image_count = 0
    image_resized = 0


    for filename in os.listdir(directory_raw):
        if filename.endswith(".jpg"):
            print("Resizing Raw JPG ({})...\n".format(filename))

            fd_img = open(directory_raw + '/' + filename, 'rb')
            img = Image.open(fd_img)
            
            img = resizeimage.resize_cover(img, [1024, 1024])
            
            img.save(directory_resized + '/1024px-' + filename, img.format)
            fd_img.close()

            if os.path.isfile(directory_resized + '/1024px-' + filename):
                image_resized = image_resized + 1

                print("File saved.")

            image_count = image_count + 1

            continue
        else:
            continue

except Exception as e:
    print("Exception Caught\n\n{}".format(e))

print("Images found: {}...\n".format(image_count))
print("Images resized: {}...\n".format(image_resized))