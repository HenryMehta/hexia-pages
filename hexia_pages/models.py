from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Page (models.Model):
    ''' Defines a Page shown through a template '''
    name = models.CharField(
        max_length=20
    )
    slug = models.SlugField(
        unique = True,
    )
    content = RichTextUploadingField()
    
    def __str__(self):
        return u'%s' % (self.name)

    class Meta:
        ordering = ['name']