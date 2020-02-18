from django.contrib import admin
from django.urls import path

# from ..POST import views
from POST import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login),
    path('register/', views.register),
    path('post/', views.post),
    path('show/', views.show),
]
