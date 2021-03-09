from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),# le '' correspond à ce qui va suivre dans l'url (localhost/myapp)
    path('about/', views.about, name='about'),
    path('jewellery/', views.jewellery, name='jewellery'),
    path('contact/', views.contact, name='contact'),
]
