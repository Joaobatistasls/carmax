# importing my urls
from django.urls import path
# importing view urls
from . import views

# creating my default urls
urlpatterns = [
    path('', views.index, name='index')
]
