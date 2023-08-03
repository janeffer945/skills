from django.urls import path
from authapp import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='handelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),



]