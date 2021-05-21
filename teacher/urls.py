from django.urls import path
from .views import teacherView

urlpatterns = [
    path('teacherData/', teacherView),
]