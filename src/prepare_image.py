import random

from PIL import Image
from tensorflow.keras.datasets import fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

image_num = random.randint(0, 10000)
example_image = test_images[image_num]

im = Image.fromarray(example_image)
im.save("data/test.png")
print(f"Test image[{image_num}] is created!")
