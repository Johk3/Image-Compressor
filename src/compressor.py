from PIL import Image
class Engine:
    def __init__(self, images, imgquality=50):
        self.images = images
        self.imgquality = imgquality

    def motor(self):
        for image in self.images:
            print(image)
            foo = Image.open("C:\\Users\\Johannes\\PycharmProjects\\Fupi-Compressor\\src\\images\\" + image)

            foo = foo.resize((foo.size), Image.ANTIALIAS)
            foo.save(str("C:\\Users\\Johannes\\PycharmProjects\\Fupi-Compressor\\src\\output\\" + image), quality=self.imgquality)