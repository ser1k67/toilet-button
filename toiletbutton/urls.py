from django.urls import path

from toiletbutton import views

urlpatterns = [
    path('', views.index, name='toilet')
]
