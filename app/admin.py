from django.contrib import admin

# Register your models here.
from .models import blogs,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','description')
    
class blogsAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','content')

admin.site.register(blogs,blogsAdmin)
admin.site.register(Category,CategoryAdmin)