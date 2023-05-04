# Imports
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
import matplotlib
from matplotlib import pyplot
matplotlib.use('SVG')
from sklearn.manifold import Isomap
from common.scripts.create_database import image_to_vector
import pandas
import numpy
import glob
import operator

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
def graph_models(images_dataframe, model_tag, k, reduced_faces):
    
    for var in images_dataframe.Keys.unique():
        pyplot.plot(reduced_faces[images_dataframe.Keys == var,0],
        reduced_faces[images_dataframe.Keys == var,1],
        linestyle = "None", marker = ".", label = var)
    
    pyplot.title(model_tag)
    pyplot.legend(bbox_to_anchor=(1.37,0.5), loc="right")
    pyplot.tight_layout()
    pyplot.savefig('/static/graphs/graph_'+str(k+1)+".jpg")
    pyplot.close()
    
# The execute_models function is in charge of the following things:
# Reduce the Images dimentionality with the different models PCA, SVD, ISOMAP.
# Check the Similarity of the Resulting Vectors to determine if the user trying
# the authentication is the correct user.
def execute_models(images_array, vectorized_image, images_dataframe, user):
    
    Models = {
    "PCA":PCA(n_components = 2),
    "SVD":TruncatedSVD(n_components = 2),
    "ISOmap": Isomap(n_components = 2)
    }
    
    similar_faces = []
    similar_faces_dict = {}
    for k, model_tag in enumerate(Models.keys()):
        
        Model = Models.get(model_tag)
        images_array_model = Model.fit(images_array)
        reduced_faces = images_array_model.transform(images_array)
        reduced_face = images_array_model.transform(vectorized_image)
        
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

        # compare_array = numpy.append(compare_array,images_dataframe.iloc[manhattanVectorIndex[0:5]]['Keys'])
        # compare_array = numpy.append(compare_array,images_dataframe.iloc[euclideanVectorIndex[0:5]]['Keys'])
        # compare_array = numpy.append(compare_array,images_dataframe.iloc[cosineVectorIndex[0:5]]['Keys'])

        for i in range(0,5):
            similar_faces.append((images_dataframe['Keys'][manhattanVectorIndex[i]], model_tag))
            similar_faces.append((images_dataframe['Keys'][euclideanVectorIndex[i]], model_tag))
            similar_faces.append((images_dataframe['Keys'][cosineVectorIndex[i]], model_tag))

    
    for index, tup in enumerate(similar_faces):
        if tup[0] not in similar_faces_dict.keys():
            if tup[1] == 'SVD':
                similar_faces_dict[tup[0]] = 0.5
            else:
                similar_faces_dict[tup[0]] = 1
        else:
            if tup[1] == 'SVD':
                similar_faces_dict[tup[0]] += 0.5
            else:
                similar_faces_dict[tup[0]] += 1

    similar_faces_dict = dict(sorted(similar_faces_dict.items(), key=operator.itemgetter(1), reverse=True))
    items_to_check = int(numpy.ceil(len(similar_faces_dict)/3))
    check_similar_face = dict(list(similar_faces_dict.items())[0:items_to_check])

    if(user in check_similar_face.keys()):
        return user
    else:
        return False
    
# Remove Keys from Dataframe.
def remove_keys(images_dataframe, profile, user):
    face=numpy.asarray(images_dataframe.iloc[:,1:])
    user_auth = execute_models(face, profile, images_dataframe, user)
    return user_auth

# Function to receive the image that the user takes in the auth system.
def image_received(image_path,user):
    image = glob.glob(image_path)
    df=pandas.read_csv("common/scripts/Faces.csv")

    vectorized_image=image_to_vector(image[0])
    if (vectorized_image is not None):
        user_auth = remove_keys(df,numpy.asarray(vectorized_image).reshape(1, -1), user)
        return user_auth
    else:
        return None

