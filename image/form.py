from django import forms

class ImageUploadingForm(forms.Form):
    image = forms.ImageField()
    