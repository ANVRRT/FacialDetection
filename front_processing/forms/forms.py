from django import forms

class ImageUploadForm(forms.Form):
    image_to_process = forms.FileField(
        widget=forms.FileInput(attrs={'accept': 'image/*', 'capture':'camera'})
    )
