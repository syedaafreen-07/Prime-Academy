from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='log'),
    path('home/', views.home, name='home'),
    path('register/',views.handleRegister,name='HandeRegister'),
    path('login/',views.handleLogin,name='HandelLogin'),
    path('contact/',views.contact,name='contact'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('enroll/<int:sno>/',views.enroll,name='enroll')

]
