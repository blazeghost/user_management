from django.urls import path, include
from . import views

urlpatterns = [
    ################# URLS ###################
    path('', views.LoginPage, name='loginpage'),
    path('registerpage/', views.RegisterPage, name='registerpage'),
    path('index/', views.IndexPage, name='indexpage'),
    path('blank/', views.Blank, name='blankpage'),
    path('visitordetails/', views.VisitorDetails, name='visitordetails'),
    path('admineditpage/<int:pk>', views.AdminEditPage, name='admineditpage'),
    path('securityeditpage/<int:pk>',
         views.SecurityEditPage, name='securityeditpage'),



    ################ FUNCTIONAL URLS ################
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('profile/<int:pk>', views.Profile, name='profile'),
    path('visitorlist/', views.VisitorList, name='visitorlist'),
    path('addvisitor/<int:pk>', views.AddVisitor, name='addvisitor'),
    path('adminedit/<int:pk>', views.AdminEditVisitor, name='adminedit'),
    path('securityedit/<int:pk>', views.SecurityEditVisitor, name='securityedit'),
    path('admindelete/<int:pk>', views.AdminDelete, name='admindelete'),
    path('securitydelete/<int:pk>', views.SecurityDelete, name='securitydelete'),
]
