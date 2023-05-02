from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.manifold import Isomap
from sklearn.metrics.pairwise import cosine_similarity
#from sklearn.manifold import TSNE
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

import face_recognition
from create_database import image_to_vector
import pandas
import numpy
import glob
import cv2

def classify_faces(images_dataframe, profile):
    face=numpy.asarray(images_dataframe.iloc[:,1:])
    dimentionality_reduction(face, profile, images_dataframe)

def dimentionality_reduction(images_array, vectorized_image, image_dataframe):
    Models = {
    "PCA":PCA(n_components = 2),
    "SVD":TruncatedSVD(n_components = 2),
    "LDA": LDA(n_components = 2),
    "ISOmap": Isomap(n_components = 2)
    }
    
    for model_tag in Models:
        Model = Models.get(model_tag)
        images_array_model = Model.fit(images_array)
        reduced_faces = images_array_model.transform(images_array)
        reduced_face = images_array_model.transform(vectorized_image)
        similarities = []
        i = 0
        for db_face in reduced_faces:
            similarity = numpy.linalg.norm(reduced_face[0]-db_face)
            #similarity = DistCos(reduced_face[0], db_face)
            similarities.append(similarity)

        #print('-------------------')
        similarities = numpy.asarray(similarities)
        Idx = numpy.argsort(similarities)
        print(image_dataframe.iloc[Idx[0:5]])

def L2(x,y):
  z = x-y
  z = z ** 2
  z = numpy.sum(z)
  return numpy.power(z,1/2)

def DistCos(x,y):
  a = numpy.matmul(x.T, y)
  b = numpy.power( numpy.matmul( x.T, x), 1/2 ) * numpy.power( numpy.matmul( y.T, y), 1/2 )
  return a/b  

def similarity_comparison(x,y, kernel):
    return kernel(x,y)

images = glob.glob("files/TC3002B_Faces/" + "**/**.jpg")
df=pandas.read_csv("Faces.csv")

pca = []
svd = []
tsne = []

print(images[2])
print('-----------------')
vectorized_image=image_to_vector(images[2])

classify_faces(df,numpy.asarray(vectorized_image).reshape(1, -1))
