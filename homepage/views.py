from django.shortcuts import render, redirect

from homepage.forms import DocumentForm
from homepage.models import Document
from imagebox.models import *

def index(request):
    return render(request, 'homepage/index.html')

def about(requet):
    return render(requet, 'homepage/about.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage:document')
    else:
        form = DocumentForm()
        documents = Document.objects.all()

        context = {'form': form,
                   'documents': documents}
    return render(request, 'homepage/model_form_upload.html', context)

def display_product_images(request):
    product_images1 = ProductImage.objects.all()
    product_images2 = ProductImage2.objects.all()
    product_images3 = ProductImage3.objects.all()
    product_images4 = ProductImage4.objects.all()

    images_list = {'product_images1': product_images1,
                   'product_images2': product_images2,
                   'product_images3': product_images3,
                   'product_images4': product_images4}
    return render(request, 'homepage/products.html', images_list)