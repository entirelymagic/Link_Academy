import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# read files
figure, axes = plt.subplots(4, 3)
current_dir = os.getcwd() + '\\players\\'
l_img = []
for root, dirs, files in os.walk(current_dir):
    files = [x for x in files if not x.startswith(".")]
    for index, imgfile in enumerate(files):
        imgpath = current_dir + imgfile
        x = index // 3
        y = index % 3
        img = mpimg.imread(imgpath)
        l_img.append(imgpath)
        axes[x, y].imshow(img)

plt.show()
