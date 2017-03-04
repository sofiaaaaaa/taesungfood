from django import forms
from imagebox.models import ProductImage

class ImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('description', 'image')