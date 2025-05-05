from django.db import models

class Iam(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    photo_small = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo for profile')
    photo_banner = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo for banner')
    edit_at = models.DateTimeField(auto_now=True, verbose_name='Edit at')

    def __str__(self):
        return self.name
    
class Work(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(blank=True, default='defaults/project_image.png', verbose_name='Image')
    link_project = models.URLField(null=True, blank=True, max_length=100, verbose_name='Link project')

    def __str__(self):
        return self.title
    
class Links(models.Model):
    title = models.CharField(max_length=15, verbose_name='Name of SN')
    social = models.URLField(max_length=100, verbose_name='Link of any social network')

    def __str__(self):
        return self.title
    
class Carousel(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True, default='No title', verbose_name='Title of image')
    image = models.ImageField(upload_to='banners/%Y/%m/%d/', verbose_name='Image for banner')

    def __str__(self):
            return self.title