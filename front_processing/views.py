from django.shortcuts import render, redirect
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
#Import urlopen
from urllib.request import urlopen

from create_database import *
import os
import re
import base64
from .forms.forms import ImageUploadForm


# Create your views here.

# def index(request):

#     print(request.POST)
#     print(request.FILES)
#     return render(request, 'front_processing/index.html', {})


def index(request):
    context = {}
    if request.method == 'POST':

        photo_name = request.POST['photo_name']
        dataURL = request.POST['image_to_process']

        image_data = re.search(r'base64,(.*)', dataURL).group(1)
        image_data = re.sub("^data:image/png;base64,", "", image_data)
        image_data = base64.b64decode(image_data)

        image_file_name = photo_name + ".png"

        X = image_to_vector(image_file_name)

        print(X)

        database = pandas.read_csv("Faces.csv")

        print(database)

        image_file_path = os.path.join('temp/images/', image_file_name)

        with open(image_file_path, 'wb') as image_file:
            image_file.write(image_data)


    return render(request, 'front_processing/index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.
    

    return render(request, 'front_processing/index.html')

# def image_upload(request):
#     context = dict()
#     if request.method == 'POST':
#         username = request.POST["username"]
#         image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
#         image = NamedTemporaryFile()
#         image.write(urlopen(path).read())
#         image.flush()
#         image = File(image)
#         name = str(image.name).split('\\')[-1]
#         name += '.jpg'  # store image in jpeg format
#         image.name = name
#         if image is not None:
#             obj = Image.objects.create(username=username, image=image)  # create a object of Image type defined in your model
#             obj.save()
#             context["path"] = obj.image.url  #url to image stored in my server/local device
#             context["username"] = obj.username
#         else :
#             return redirect('/')
#         return redirect('any_url')
#     return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.         