from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, RegisterFinView
from advert.views import ResponseList

urlpatterns = [
    path('', ResponseList.as_view(), name="responselist"),
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('register/',
         RegisterView.as_view(),
         name='register'),
    path('finish/',
         RegisterFinView.as_view(),
         name='registerfin'),

]
