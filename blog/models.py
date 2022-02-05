from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
def upload_location(instance, filename):
    return "posts/{filename}".format(filename=filename)

class AllCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class EachCategory(models.Model):
    Course = models.CharField(max_length=250,blank=False, default='')
    category = models.ForeignKey(AllCategory, on_delete=models.CASCADE,related_name='Course')
    Title = models.CharField(max_length=250,blank=False, default='', unique=True)
    Blogdetails = models.TextField()
    Image = models.ImageField(_('Image'),upload_to=upload_location, blank=True, default='posts/default.png')
    start_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('Course',)   
    def __str__(self):
        return self.category