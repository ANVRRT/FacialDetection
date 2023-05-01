from IPython.lib.display import FileLinks
import pandas
import cv2
import face_recognition
import glob
import numpy

# The Database is created only once.

# This class is to set the options for the file search.
class Option:
    folder_path = None
    out_file = None

# Design the Database for Face Recognition.
def design_database(options):
    # Folder path of all the images.
    folder_path = options.folder_path  
    # Select only the images that has JPG extension.
    images = glob.glob(folder_path + "**/**.jpg")
    # Name of the DataBase File
    out_file = options.out_file  
    # Empty Database
    database = []  
    # Persons Labels  
    keys = [] 
    for image in images:
        # Read the Face Image and keep it on the database as a Vector Image.
        vector_image = image_to_vector(image)
        database.append(vector_image)

        keys.append(str(image).split("/")[1].split("\\")[1])

    # Create DataFrame with the labels and vector images to convert it to CSV file.
    dataframe = pandas.DataFrame(database)
    dataframe.insert(0, "Keys", keys)
    dataframe.to_csv(out_file, index=False)

# Convert the Image to Vector
def image_to_vector(File):

    # Read the image from the File. 
    image = cv2.imread(File)  

    # Aspect Ratio
    aspect_ratio = 480 / image.shape[1]  
    width = int(image.shape[1] * aspect_ratio)
    height = int(image.shape[0] * aspect_ratio)

    # Reescale the image.
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
    
    # Save the temporal rescale image.
    cv2.imwrite("temporal_image.jpg", image)

    # Load the rescale image.
    rescale_image = face_recognition.load_image_file("temporal_image.jpg")

    # Locate the bounding boxes of human faces in a image and returns the array.
    locations = face_recognition.face_locations(rescale_image)

    # Give an image, return the 128-dimension face encoding for each face in the image.
    face_vectors = face_recognition.face_encodings(rescale_image, locations)

    # Save the face vector.
    face_vector = face_vectors[0]

    # return the face vector.
    return face_vector


if __name__ == '__main__':

    # Create an Option object to set the options for searching the files. 
    options = Option

    options.folder_path = "files/TC3002B_Faces/"
    options.out_file = "Faces.csv"

    # Create and Design the Database.
    design_database(options)
