from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name = 'logout'),
    path('contact/',views.ContactPage,name='contact'),
    path('about/',views.AboutPage,name='about')
]