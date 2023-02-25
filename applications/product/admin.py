from django.contrib import admin
from .models import Category , Product, Brand
from django.utils.safestring import mark_safe

admin.site.register(Brand)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['name','slug']
    prepopulated_fields = {'slug' : ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','image_show','price','currency','avialable','created','uploaded']
    list_filter = ['avialable','created','uploaded']
    list_editable = ['price', 'avialable']
    prepopulated_fields = {'slug':('name',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"
    image_show.__name__= "Картинка"