from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
#import matplotlib
#matplotlib.use("Agg")
from matplotlib import pyplot
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

def graph_models(images_dataframe, model_tag, k, ax, reduced_faces):
    ax[k].set_title(model_tag)
    for var in images_dataframe.Keys.unique():
        ax[k].plot(reduced_faces[images_dataframe.Keys == var,0],
        reduced_faces[images_dataframe.Keys == var,1],
        linestyle = "None", marker = ".", label = var)
    pyplot.title(model_tag)

def dimentionality_reduction(images_array, vectorized_image, images_dataframe):
    Models = {
    "PCA":PCA(n_components = 2),
    "SVD":TruncatedSVD(n_components = 2),
    "ISOmap": Isomap(n_components = 2)
    }
    
    fig, ax = pyplot.subplots(1,3, figsize = [16,6] )

    for k, model_tag in enumerate(Models.keys()):
        Model = Models.get(model_tag)
        images_array_model = Model.fit(images_array)
        reduced_faces = images_array_model.transform(images_array)
        reduced_face = images_array_model.transform(vectorized_image)
        graph_models(images_dataframe, model_tag, k, ax, reduced_faces)
        similaritiesManhattan = []
        similaritiesEuclidean = []
        similaritiesCosine = []
        for db_face in reduced_faces:
            similarityManhattan = manhattan(reduced_face[0],db_face)
            similarityEuclidean = L2(reduced_face[0],db_face)
            similarityCosine = DistCos(reduced_face[0], db_face)
            similaritiesManhattan.append(similarityManhattan)
            similaritiesEuclidean.append(similarityEuclidean)
            similaritiesCosine.append(similarityCosine)

        similaritiesManhattan = numpy.asarray(similaritiesManhattan)
        similaritiesEuclidean = numpy.asarray(similaritiesEuclidean)
        similaritiesCosine = numpy.asarray(similaritiesCosine)
        
        manhattanVectorIndex = numpy.argsort(similaritiesManhattan)
        euclideanVectorIndex = numpy.argsort(similaritiesEuclidean)
        cosineVectorIndex = numpy.argsort(similaritiesCosine)[::-1]

        print('MANHATTAN WITH MODEL -- ' + model_tag)
        print(images_dataframe.iloc[manhattanVectorIndex[0:5]])
        print('EUCLIDEAN WITH MODEL -- ' + model_tag)
        print(images_dataframe.iloc[euclideanVectorIndex [0:5]])
        print('COSINE SIMILARITY WITH MODEL -- ' + model_tag)
        print(images_dataframe.iloc[cosineVectorIndex [0:5]])

    label=images_dataframe.Keys.unique()
    fig.legend([ax[0], ax[1], ax[2]],
    labels=label,
    loc = "right"
    )
    pyplot.show()

def L2(x,y):
  z = x-y
  z = z ** 2
  z = numpy.sum(z)
  return numpy.power(z,1/2)

def DistCos(x,y):
  a = numpy.matmul(x.T, y)
  b = numpy.power( numpy.matmul( x.T, x), 1/2 ) * numpy.power( numpy.matmul( y.T, y), 1/2 )
  return a/b  

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))


images = glob.glob("files/TC3002B_Faces/" + "**/**.jpg")
df=pandas.read_csv("Faces.csv")

pca = []
svd = []
tsne = []

print(images[41])
print('-----------------')
vectorized_image=image_to_vector(images[41])

classify_faces(df,numpy.asarray(vectorized_image).reshape(1, -1))
