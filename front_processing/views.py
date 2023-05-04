from django.shortcuts import render, redirect
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
#Import urlopen
from urllib.request import urlopen

import os
import re
import base64
# from .forms.forms import ImageUploadForm

from common.scripts.image_processing import image_received




# Create your views here.

# def index(request):

#     print(request.POST)
#     print(request.FILES)
#     return render(request, 'front_processing/index.html', {})


def index(request):
    request.session["matricula"] = None

    context = {}
    if request.method == 'POST':

        photo_name = request.POST["matricula"]
        dataURL = request.POST['image_to_process']

        image_data = re.search(r'base64,(.*)', dataURL).group(1)
        image_data = re.sub("^data:image/png;base64,", "", image_data)
        image_data = base64.b64decode(image_data)

        image_file_name = photo_name + ".jpg"

        image_file_path = os.path.join('static/temp/', image_file_name)

        with open(image_file_path, 'wb') as image_file:
            image_file.write(image_data)

        print(image_file_path, photo_name)
        
        result = image_received(image_file_path, photo_name)
        if photo_name == result: # IDK what TF is going to return here
            # Save as session variable
            request.session["matricula"] = result



            return redirect("front_processing:admin")
        else:
            return redirect("front_processing:index")

    return render(request, 'front_processing/index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.
    
def admin_dashboard(request):
    if not request.session["matricula"]:
        return redirect("front_processing:index")
    
    context = {
        "matricula": request.session["matricula"]
    }




    return render(request, 'admin/index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.


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