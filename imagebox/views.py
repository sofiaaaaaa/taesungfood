from django.shortcuts import render, redirect

from imagebox.models import *
from imagebox.form import ImageForm

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imagebox:image_upload')
    else:
        form = ImageForm()
        uploaded_images1 = ProductImage.objects.all()
        uploaded_images2 = ProductImage2.objects.all()
    return render(request, 'imagebox/image.html', {
        'form': form,
        'uploaded_images1': uploaded_images1,
        'uploaded_images2': uploaded_images2
    })