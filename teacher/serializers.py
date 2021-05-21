from rest_framework import serializers
from .models import teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = (
            'id',
            'username',
            'category', 
            'numb_of_subs', 
            'about',
            'price1',
            'price2',
            'price3',
            'slug',
            'usr_pic'
            )