import src.compressor as engine
import os

images = []

for image in os.listdir("src/images"):
    images.append(image)

armed = engine.Engine(images, 50)
armed.motor()
