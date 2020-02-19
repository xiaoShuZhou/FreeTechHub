from django.contrib import admin
from django.urls import path

# from ..POST import views
from POST import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login),
    path('register/', views.register),
    path('post/<int:user_id>/', views.post),
    path('show/<int:user_id>/', views.show),
]
