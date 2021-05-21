from django.contrib import admin
from .models import teacher

class tchregAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'username',
            'category', 
            'numb_of_subs', 
            'about',
            'price1',
            'price2',
            'price3',
            'slug',
            'user_pic'
            )

# Register your models here.
admin.site.register(teacher)