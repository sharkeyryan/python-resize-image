from PIL import Image
from resizeimage import resizeimage

try:
    print("================\n{}\n================".format("Testing Resize Cover..."))

    with open('tests/test-image.jpeg', 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [200, 100])
            cover.save('test-images/test-image-cover.jpeg', image.format)

except Exception as e:
    print("================\nException Caught\n{}\n================".format(e))
