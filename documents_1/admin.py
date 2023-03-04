from django.contrib import admin
from .models import Document, Image


class DocumentAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'category', 'number', 'image', 'dateCreate']
    list_display = ['title', 'category', 'number', 'dateCreate']


class ImageAdmin(admin.ModelAdmin):
    fields = ['file']
    list_display = ['file'] #, 'get_file']

    # def get_file(self, obj):
    #     return file(f'<img src={obj.file.url} ')

    # get_file.short_discription = "Изображение"    




    
    
    

admin.site.register(Document, DocumentAdmin)
admin.site.register(Image, ImageAdmin)

# Register your models here.
