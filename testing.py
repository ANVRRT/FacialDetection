import glob
from matplotlib import pyplot
import skimage
import numpy


Files = glob.glob("./files/TC3002B_Faces/*/*.jpg")

fig, ax = pyplot.subplots(7,7, figsize = [9,6] );

print(len(Files), ax.size)
ny = 600;


for k in range(len(Files)):
  I = skimage.io.imread(Files[k])
  nx = I.shape[1]/I.shape[0] * ny 
  I = skimage.transform.resize(I, (ny,nx))
  j = k // ax.shape[0]
  i = k % ax.shape[0]
  ax[i,j].imshow(I)
  ax[i,j].axis("off")
  ax[i,j].set_title(Files[k].split("/")[2].split("\\")[1])

pyplot.show()

