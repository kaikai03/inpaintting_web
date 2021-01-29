from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("C:/Users/fakeQ/Desktop/2.png")
img_grey = img.convert('L')
img_a = img.convert('RGBA')

mat_grey = np.asarray(img_grey)
threshold = np.average(mat_grey)*0.8


x, y = img.size

for i in range(x):
    for k in range(y):
        color = img_a.getpixel((i, k))
        if np.sum(color[:3])/3 > threshold:
            color = color[:-1] + (25, )
        else:
            color = color[:-1] + (255,)
        img_a.putpixel((i, k), color)


# img_a.save("C:/Users/fakeQ/Desktop/1_deal.PNG")

plt.figure(12)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img_a)
plt.show()
