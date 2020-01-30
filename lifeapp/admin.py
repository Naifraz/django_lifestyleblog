from django.contrib import admin
from .models import author,category,article,comment,Contatct

# Register your models here.
class authorModel1(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        Model=author

admin.site.register(author,authorModel1)
class articleModel1(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]
    list_filter = ["posted_on","category"]
    class Meta:
        Model=article
admin.site.register(article,articleModel1)
class categoryModel1(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=category
admin.site.register(category,categoryModel1)
class commentModel1(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=comment
admin.site.register(comment,commentModel1)

admin.site.register(Contatct)


