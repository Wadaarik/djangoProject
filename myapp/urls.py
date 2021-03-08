from . import views
from django.urls import path

urlpatterns=[
    path('', views.index)# le '' correspond à ce qui va suivre dans l'url (localhost/myapp)
]