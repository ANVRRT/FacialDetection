from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
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
    #print(df["Keys"])
    #face = images_dataframe[images_dataframe['Keys'] == profile]
    #neighbors=len(face['Keys'])-1
    #print(face['Keys'])
    #face = numpy.asarray(face.iloc[:,1:])
    #print(face.shape)
    face=numpy.asarray(images_dataframe.iloc[:,1:])

    dimentionality_reduction(face, profile, images_dataframe)

def dimentionality_reduction(images_array, vectorized_image, image_dataframe):
    Models = {
    "PCA":PCA(n_components = 2),
    "SVD":TruncatedSVD(n_components = 2),
    #"TSNE": TSNE(n_components = 2)
    "ISOmap": Isomap(n_components = 2)
    }
    
    for model_tag in Models:
        #print(model_tag)
        Model = Models.get(model_tag)
        images_array_model = Model.fit(images_array)
        reduced_faces = images_array_model.transform(images_array)
        reduced_face = images_array_model.transform(vectorized_image)
        #print(reduced_face)
        similarities = []
        i = 0
        for db_face in reduced_faces:
            #similarity = numpy.linalg.norm(reduced_face[0]-db_face)
            similarity = DistCos(reduced_face[0], db_face)
            similarities.append(similarity)
            print(i, similarity)
            i += 1

        #print('-------------------')
        #similarities = numpy.asarray(similarities)
        #Idx = numpy.argsort(similarities)
        #print(image_dataframe.iloc[Idx[0:5]])
        print('-----------------------')
        #if model_tag == "PCA": #JALA
        #    pca.append(images_array_model)
        #if model_tag == "SVD": #JALA
        #    svd.append(images_array_model)
        #if model_tag == "TSNE": #JALA
        #    tsne.append(images_array_model)

    #pyplot.show()
    #print(numpy.asareductions[0])
    #print("#####")
    #print(reductions)

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

#for var in df.Keys.unique():
#    classify_faces(df,var)

#print(pca)
#print("###############")
#print(svd)
#print("###############")
##print(tsne[0].shape)
#print(tsne)

#images[0] es una ruta de prueba para la vectorizacion y reduccion individual de dimensiones de imagen
print(images[2])
print('-----------------')
vectorized_image=image_to_vector(images[2])
#image_reduction(numpy.asarray(vectorized_image).reshape(1, -1))

classify_faces(df,numpy.asarray(vectorized_image).reshape(1, -1))
#print(numpy.asarray(vectorized_image).reshape(1, -1))
#print("-----------------------------------")
#dimentionality_reduction(numpy.asarray(vectorized_image).reshape(1,-1),1)
