import numpy as np
import os
import time
from PIL import Image

start = time.time()
maindir = "/home/luoyuqi/shared/TextLogo3K_v2/test"
s = []
n = []
z = 0

for root, dirs, files in os.walk(maindir):
    for file in files:
        s.append(os.path.join(root, file))
for x in s:
    if ".npy" in x:
        data = np.load(x)
        n.append(data)
    if ".png" in x:
        img = Image.open(x)
        img_array = img.load()
end = time.time()
# print(z)
# print(n)
# print(s)
print('time cost:', end - start, 's')
