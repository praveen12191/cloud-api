from django.urls import path,include
from .import views
urlpatterns = [
    path('details/',views.details),
    path('getDetails/',views.getDetails),
    path('userdetail/',views.userDetails)
]
