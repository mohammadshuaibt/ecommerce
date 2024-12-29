from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name = 'logout'),
    path('contact/',views.ContactPage,name='contact'),
    path('about/',views.AboutPage,name='about'),
    path('register/',views.register_page,name='register'),
    path('product/<int:pk>',views.product_details,name='product_details'),
    path('category/<str:namee>',views.category,name = 'category'),
    path('profile/',views.profile_page,name='profile'),
    path('editprofile/',views.edit_profile,name='edit_profile'),
    path('updatepassword/',views.update_password,name='update_password'),
]