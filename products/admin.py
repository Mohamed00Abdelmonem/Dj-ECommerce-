from django.contrib import admin
from .models import Product, Categories, ProductImages, Reviews
# Register your models here.



class PersonAdmin(admin.ModelAdmin):
    list_filter = ["categore"]
    search_fields = ["name"]


admin.site.register(Categories)
admin.site.register(Product, PersonAdmin)
admin.site.register(ProductImages)
admin.site.register(Reviews)    