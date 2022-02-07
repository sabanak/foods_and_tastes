from django.contrib import admin
from shop.models import categ, products
from django.urls import reverse


# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name','slug']
admin.site.register(categ,catadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name','slug','price','stock','available','img']
    list_editable=('price','stock','available','img')
admin.site.register(products,prodadmin)
