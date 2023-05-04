# Imports
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from matplotlib import pyplot
from sklearn.manifold import Isomap
from create_database import image_to_vector
import pandas
import numpy
import glob

# Function Vectors Similarity. 

# Euclidean Distance Function.
def euclidean_distance(vector_x,vector_y):
  resulting_distance = vector_x - vector_y
  resulting_distance = resulting_distance ** 2
  resulting_distance = numpy.sum(resulting_distance)
  resulting_distance = numpy.power(resulting_distance,1/2)

  return resulting_distance

# Cosine Similarity Function.
def cosine_similarity(vector_x, vector_y):
  matrix_product_result = numpy.matmul(vector_x.T, vector_y)
  product_euclidean_norm = numpy.power( numpy.matmul( vector_x.T, vector_x), 1/2 ) * numpy.power( numpy.matmul( vector_y.T, vector_y), 1/2 )

  return matrix_product_result/product_euclidean_norm  

# Manhattan Similarity Function.
def manhattan(vector_x, vector_y):

    return sum(abs(component_x-component_y) for component_x, component_y in zip(vector_x,vector_y))

# Create the graphs of each model.
#def graph_models(images_dataframe, model_tag, k, ax, reduced_faces):
#    ax[k].set_title(model_tag)
#    for var in images_dataframe.Keys.unique():
#        ax[k].plot(reduced_faces[images_dataframe.Keys == var,0],
#        reduced_faces[images_dataframe.Keys == var,1],
#        linestyle = "None", marker = ".", label = var)
#    pyplot.title(model_tag)
def graph_models(images_dataframe, model_tag, k, reduced_faces):
    
    for var in images_dataframe.Keys.unique():
        pyplot.plot(reduced_faces[images_dataframe.Keys == var,0],
        reduced_faces[images_dataframe.Keys == var,1],
        linestyle = "None", marker = ".", label = var)
    
    pyplot.title(model_tag)
    pyplot.legend(bbox_to_anchor=(1.37,0.5), loc="right")
    pyplot.tight_layout()
    pyplot.savefig('graph'+str(k+1)+".jpg")
    pyplot.close()

# The execute_models function is in charge of the following things:
# Reduce the Images dimentionality with the different models PCA, SVD, ISOMAP.
# Check the Similarity of the Resulting Vectors to determine if the user trying
# the authentication is the correct user.
def execute_models(images_array, vectorized_image, images_dataframe):
    
    Models = {
    "PCA":PCA(n_components = 2),
    "SVD":TruncatedSVD(n_components = 2),
    "ISOmap": Isomap(n_components = 2)
    }
    
    #fig, ax = pyplot.subplots(1,3, figsize = [16,6] )

    for k, model_tag in enumerate(Models.keys()):
        
        Model = Models.get(model_tag)
        images_array_model = Model.fit(images_array)
        reduced_faces = images_array_model.transform(images_array)
        reduced_face = images_array_model.transform(vectorized_image)
        
        #graph_models(images_dataframe, model_tag, k, ax, reduced_faces)
        graph_models(images_dataframe, model_tag, k, reduced_faces)
        
        similaritiesManhattan = []
        similaritiesEuclidean = []
        similaritiesCosine = []
        
        for db_face in reduced_faces:
            similarityManhattan = manhattan(reduced_face[0],db_face)
            similarityEuclidean = euclidean_distance(reduced_face[0],db_face)
            similarityCosine = cosine_similarity(reduced_face[0], db_face)
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
        print(images_dataframe.iloc[manhattanVectorIndex[0:5]]['Keys'])
        print('EUCLIDEAN WITH MODEL -- ' + model_tag)
        print(images_dataframe.iloc[euclideanVectorIndex [0:5]]['Keys'])
        print('COSINE SIMILARITY WITH MODEL -- ' + model_tag)
        print(images_dataframe.iloc[cosineVectorIndex [0:5]]['Keys'])

    
    #label=images_dataframe.Keys.unique()
    #fig.legend([ax[0], ax[1], ax[2]],labels=label,loc = "right")
    #pyplot.savefig('fig_1'+".jpg")
    #pyplot.show()

# Remove Keys from Dataframe.
def remove_keys(images_dataframe, profile):
    face=numpy.asarray(images_dataframe.iloc[:,1:])
    execute_models(face, profile, images_dataframe)

# Function to receive the image that the user takes in the auth system.
def image_recept(image_path):
    
    df=pandas.read_csv("Faces.csv")

    vectorized_image=image_to_vector(image_path[0])

    remove_keys(df,numpy.asarray(vectorized_image).reshape(1, -1))

images = glob.glob("../files/TC3002B_Faces/" + "**/**.jpg")
image_recept(images)
