from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import Isomap
#from sklearn.manifold import TSNE
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from matplotlib import pyplot

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

    dimentionality_reduction(face, profile)

def image_reduction(vectorized_image):
    Models = {
    "PCA":PCA(n_components = 2),
    "SVD":TruncatedSVD(n_components = 2),
    #"TSNE": TSNE(n_components = 2)
    }

    for model_tag in Models:
        #print(model_tag)
        Model = Models.get(model_tag)
        #images_array_model = Model.fit_transform(vectorized_image)
        #reduced_face = images_array_model.transform(images_array)

        if model_tag == "PCA": #JALA
            reduced_face = Model.transform(vectorized_image)
            pca.append(reduced_face)
        if model_tag == "SVD": #JALA
            reduced_face = Model.transform(vectorized_image)
            svd.append(reduced_face)
        if model_tag == "TSNE": #JALA
            images_array_model = Model.fit_transform(vectorized_image)
            tsne.append(images_array_model)

def dimentionality_reduction(images_array, vectorized_image):
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
        print(reduced_face)

        #if model_tag == "PCA": #JALA
        #    pca.append(images_array_model)
        #if model_tag == "SVD": #JALA
        #    svd.append(images_array_model)
        #if model_tag == "TSNE": #JALA
        #    tsne.append(images_array_model)

    #pyplot.show()
    #print(numpy.asareductions[0])
    print("#####")
    #print(reductions)

def similarity_comparison():
    pass

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
vectorized_image=image_to_vector(images[0])
#image_reduction(numpy.asarray(vectorized_image).reshape(1, -1))

classify_faces(df,numpy.asarray(vectorized_image).reshape(1, -1))
#print(numpy.asarray(vectorized_image).reshape(1, -1))
#print("-----------------------------------")
#dimentionality_reduction(numpy.asarray(vectorized_image).reshape(1,-1),1)
