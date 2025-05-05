from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('work/<int:pk>/json/', work_detail_json, name='work_detail_json'),
]
