from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize

class ProductImage(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(50, 50)],
        format='JPEG',
        options={'quality': 60}),
    smart = ImageSpecField(
        source='image',
        processors=[SmartResize(50, 50)],
        format='JPEG'
    )

    def __str__(self):
        return  self.description

class ProductImage2(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(50, 50)],
        format='JPEG',
        options={'quality': 60}),
    smart = ImageSpecField(
        source='image',
        processors=[SmartResize(50, 50)],
        format='JPEG'
    )

    def __str__(self):
        return self.description

class ProductImage3(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(50, 50)],
        format='JPEG',
        options={'quality': 60}),
    smart = ImageSpecField(
        source='image',
        processors=[SmartResize(50, 50)],
        format='JPEG'
    )

    def __str__(self):
        return self.description

class ProductImage4(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(50, 50)],
        format='JPEG',
        options={'quality': 60}),
    smart = ImageSpecField(
        source='image',
        processors=[SmartResize(50, 50)],
        format='JPEG'
    )

    def __str__(self):
        return self.description

#profile = ProductImage.objects.all()[0]
#print(profile.avatar_thumbnail.url) # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
#print(profile.avatar_thumbnail.width) # > 100

# without Models
from imagekit import ImageSpec, register

class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 50)]
    format = 'JPEG'
    options = {'quality': 60}

#register.generator('imagebox:thumbnail', Thumbnail) # to generate processed image file directly in template

#source_file = open('/path/to/myimage.jpg')
#image_generator = Thumbnail(source=source_file)
#result = image_generator.generate()

#to save the image
#dest = open('/path/to/dest.jpg', 'w')
#dest.write(result.read())
#dest.close()

"""
# Don't save original image
from imagekit.models import ProcessedImageField

class Profile(models.Model):
    avatar_thumbnail = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality': 60})
"""